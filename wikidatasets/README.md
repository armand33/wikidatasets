# WikiDataSets

This project provides topical knowledge graphs extracted from WikiData database dumps. 

### Data sets
Data sets are available on this [page](https://graphs.telecom-paristech.fr/Home_page.html#wikidatasets-section).

### Usage
The `example/` folder contains examples of scripts to create datasets (e.g. [build_humans.py](https://github.com/armand33/WikiDataSets/blob/master/examples/build_humans.py)).
Such scripts should be placed in the main directory (along with `utils.py`, `processFunctions.py`) and hard-coded paths should be tuned to match your installation.

This script 

### Requirements
The code was developed and tested on Python 3.7. The following Python libraries are required.

Dependencies:
* [pandas](https://pypi.org/project/pandas/)
* [tqdm](https://pypi.org/project/tqdm/)
* [SPARQLWrapper](https://pypi.org/project/SPARQLWrapper/)

Standard Python library :
* bz2
* pickle
* json

### Citations
If you find this code useful in your research, please consider citing our [paper](https://arxiv.org/abs/1906.04536):
```  
  @misc{arm2019wikidatasets,
      title={WikiDataSets : Standardized sub-graphs from WikiData},
      author={Armand Boschin},
      year={2019},
      eprint={1906.04536},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
  }
```

### Authors
* **Armand Boschin** - *Initial work* - [Github](https://github.com/armand33)
