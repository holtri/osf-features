# OSF Feature Extraction
_Scripts to create outlier scoring function feature data sets_

This repository contains code to calculate different outlier scoring functions (OSF) with the [ELKI framework](https://elki-project.github.io/).

## Reproducing the feature data

Steps to generate the feature data from raw measurements:

Configuration: Set data input and output directories in `src/config.py`. Expected input format:
```
/somepath/input/DataSetA/a1.csv
/somepath/input/DataSetA/a2.csv
/somepath/input/DataSetB/b1.csv
/somepath/input/DataSetB/b2.csv
```
For more information on the `.csv` format see [ELKI documentation](https://elki-project.github.io/howto/inputformat`) 

Requirements: `python3.7`, `pipenv` and `java`. 
 
1. Run `pipenv install` to fetch all python dependencies.
2. Run `pipenv run osf` to calculate the features. 
This automtaically fetches the [ELKI binary](https://elki-project.github.io/releases/).
Computes the features for `INPUT_ROOT` and writes the results to `OUTPUT_ROOT`.