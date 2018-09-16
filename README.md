Pytorch implementation of Neural Scene and rendering
---
### About this project

#### Structure
```
.
├──docs
├── main.py
├── pytorch_deep_learning
│   ├── __init__.py
│   ├── models
│   │   ├── generative_architectures.py
│   │   ├── generative_query_network.py
│   │   ├── __init__.py
│   │   └── representation_architectures.py
│   ├── training.py
│   └── utils
│       ├── data_transform.py
│       └──__init__.py
|── README.md
├── requirements.txt
├── test
│   ├── __init__.py
│   ├── test_data_transform.py
│   ├── test_gpu_setup.py
│   └── test_unittest.py
└── tools
    └── download_data.py
```

#### Contribution

### Dataset

#### Download data - an easy way with one step

#### A comprehensive list of all data

### Requirements

##### 1. Using virtual environment with `Anaconda`

##### 2. Using `setuptools`

### Run the program
Simply as follows
```bash
python main.py --data_path=<path_to_downloaded_data>
```

For further details of arguments, try with `--help`
```bash

$python main.py --help                                                                                                                                                                                                                                                   [
usage: main.py [-h] [--iterations ITERATIONS] [--batch_size BATCH_SIZE]
               [--data_path DATA_PATH] [--model_path MODEL_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --iterations ITERATIONS
                        A number of batches to complete one epoch (Default:
                        20,000).
  --batch_size BATCH_SIZE
                        A number of examples used for one batch. (Default: 36)
  --data_path DATA_PATH
                        A path to directory of training data
  --model_path MODEL_PATH
                        A path to directory to save a model with a timestamp.
```

### Future work

### References
