# MolCompass Chemical Space Projection

Projects any molecule, given as a SMILES string, onto a 2D map of chemical space using a pre-trained parametric t-SNE neural network. The projection is deterministic: structurally similar compounds consistently cluster together, based on 2048-bit ECFP fingerprints (radius=3) and a network trained on 1.56 million ChEMBL v.23 structures. Useful for exploring chemical space, checking a QSAR/QSPR models applicability domain, and spotting model cliffs where structurally similar compounds get inconsistent predictions.



## Information
### Identifiers
- **Ersilia Identifier:** `eos19dk`
- **Slug:** `molcompass`

### Domain
- **Task:** `Representation`
- **Subtask:** `Projection`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`, `Fingerprint`, `Similarity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** X and Y coordinates locating the molecule within the pretrained parametric t-SNE chemical-space map.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| x | float |  | X-coordinate of the molecule in the pretrained parametric t-SNE chemical space map |
| y | float |  | Y-coordinate of the molecule in the pretrained parametric t-SNE chemical space map |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`

### Resource Consumption


### References
- **Source Code**: [https://github.com/sergsb/molcomplib](https://github.com/sergsb/molcomplib)
- **Publication**: [https://doi.org/10.1186/s13321-024-00888-z](https://doi.org/10.1186/s13321-024-00888-z)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos19dk
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos19dk
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
