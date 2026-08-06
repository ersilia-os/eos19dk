import os
import pickle

import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

CHECKPOINTS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "checkpoints"
)
CHECKPOINT_PATH = os.path.join(CHECKPOINTS_DIR, "ecfp_3_2048_2d.pkl")


def _smiles_to_ecfp(smiles, radius=3, n_bits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
    arr = np.zeros((1, n_bits))
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


def _dense(x, w, b):
    return x.dot(w) + b


def _batchnorm(x, gamma, beta, running_mean, running_var, eps=1e-5):
    x = (x - running_mean) / np.sqrt(running_var + eps)
    return x * gamma + beta


def _relu(x):
    return np.maximum(x, 0)


class MolCompassProjector:
    """Pretrained parametric t-SNE network projecting ECFP fingerprints to 2D coordinates."""

    def __init__(self, checkpoint_path=CHECKPOINT_PATH):
        with open(checkpoint_path, "rb") as f:
            self.parameters = pickle.load(f)

    def _forward(self, x):
        for layer in range(1, 5):
            w = self.parameters["fc{}.weight".format(layer)].transpose(1, 0)
            b = self.parameters["fc{}.bias".format(layer)]
            x = _dense(x, w, b)
            if layer != 4:
                x = _batchnorm(
                    x,
                    self.parameters["bn{}.weight".format(layer)],
                    self.parameters["bn{}.bias".format(layer)],
                    self.parameters["bn{}.running_mean".format(layer)],
                    self.parameters["bn{}.running_var".format(layer)],
                )
                x = _relu(x)
        return x

    def project(self, smiles):
        ecfp = _smiles_to_ecfp(smiles)
        if ecfp is None:
            return np.array([np.nan, np.nan], dtype=np.float32)
        coords = self._forward(ecfp)
        return coords.astype(np.float32)


def predict(smiles_list):
    projector = MolCompassProjector()
    return [projector.project(smi) for smi in smiles_list]
