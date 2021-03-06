
---


### About


 This is a Pytorch implementation of a vanilla Generative Query Network from "Neural scene representation and rendering", a computer vision system is similar to Recurrent Variational Auto Encoder with two levels of representation learned by Convolutional Neural Network), with to tackle a challenge of object recognization in 3D stimulation world.

 **Disclaimer**: In this version (v1), I set a scope to improve the quality of code by designing modules, clarifying assumptions with refactorization and replication from another [open source project](https://github.com/wohlert/generative-query-network-pytorch). Further work will be probably added and built on top of this repository, not solely generative query network.

(IMAGE)

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

### A short guide to a virtual environment with Anaconda

Here we create a virtual environment with `Anaconda`, a manager to distribute packages with different versions and dependencies by creating a capsule to include all you need in one folder.

To download and install, type the below into your terminal. It will help you download into and and then set up seamlessly ath `~/home/anaconda`.  orig
```bash
$ bash scripts/download_and_setup_anaconda.sh
```
To install a virtual environment named "pytorch_deep_learning" for the source code, use the following command.
```bash
$ conda env create --file imagination.yml
```

By this command, `anaconda` will run a process of installations for all necessary packages needed for your computer. Then, to activate the virtual environment, type:

```bash
$ source activate imagination_py36
```

To deactivate an environment, simply do

```bash
$ source deactivate
```

### Dataset

#### Download data - an easy way with one step

Here I provide a one-step preparation for you to (almost) immediately jump into the code. Only make sure that you have a good internet connection and around 68MB storage (For a full data set, it is about 24 GB)

```bash
$ python tools/download_data.py --data_path=<path_to_your_data_directory>
```

#### Shepard Metzler 7 parts

The tiny preprocessed dataset described as above is extracted from Shepard Metzler with 7 parts composed of 7 randomly color cubes in three dimension grid with yaw (vertical axes) and pitch (transverse axes) followed by a position.

The famous story of this data set comes from an idea of cognitive neuroscience to study a cognitive task of a human to rotate an imaginary object from a few observations. Here, the tasks is reconstructing several 2D images from projections of a 3D object.

(IMAGE)
```bash
$ bash scripts/download_small_shepard_metzler.sh
```

Run this test to make sure that you've got the right data
```python
$ python -m unittest test.test_download_data
```

If there is no error, it means you are welcomed to move to the next part.If not, feel free to create an issue and send the log of report to let us know what's wrong with your data.

##### A comprehensive list of 7 datasets available for you to try

Checkout this [repository of DeepMind lab](https://github.com/deepmind/gqn-datasets) for more information. This would require you to install some more packages such as `tensorflow` and `gsutils`. Following the instructions inside, you will be able to download 1.45 TB of raw data in total.  Since this is an implementation of `pytorch`, another extra step needed is converting those into tensor readable by our framework. Try this [open-source repository](https://github.com/l3robot/gqn_datasets_translator)

### Run the program
Warning: This source code is built on top of using one GPU with high memory GPU from 16GB (P100 or M40 for example). Please make sure that you have an appropriate infrastructure for running this source code.

To get started, simply open your terminal and type the following command line
```bash
$ python main.py --data_path=<path_to_downloaded_data>
```

For further details of arguments, try with `--help`

```bash

$ python main.py --help                                                                                                                                                                                                                                                   [
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

For `--gradient_steps=1000`, expected result should look like

![](./docs/sample_reconstruction_1000.jpg)

### What's next?

Some of couple ideas to improve this source code. For example:

* Reduce running time by running multiple GPUs and data parallel with CPUs.

* Integrate this source code with deep reinforcement learning with a stimulated 3D game.

* Incoporate with other metric to derive a better learners of representation.

### References

#### Paper

Eslami, SM Ali, et al. "Neural scene representation and rendering." Science 360.6394 (2018): 1204-1210.

Shepard, Roger N. and Joerg Metzler. “Mental rotation of three-dimensional objects.” Science 171 3972 (1971): 701-3.

Another `pytorch` implementation: https://github.com/wohlert/generative-query-network-pytorch
