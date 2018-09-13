"""
The main file to execute source code

Usage: $python main.py
"""

import argparse

import torch

from pytorch_deep_learning.utils.data_loader import ShepardMetzler
from pytorch_deep_learning.models.generative_query_network import GenerativeQueryNetwork
from pytorch_deep_learning.training import ModelTrainer

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def parse_args():
    parser = argparse.ArgumentParser(description="pytorch_deep_learning")

    parser.add_argument("--iterations", type=int, default=20000, \
        help="Number of batches to complete one epoch (Default: 20,000).")
    parser.add_argument("--batch_size", type=int, default=36, \
        help="Number of examples used for one batch.")
    parser.add_argument("--data_path", type=str, default="./data/train", \
        help="Path to directory of training data ")
    parser.add_argument("--model_path", type=str, default="./model", \
        help="Path to directory to save model with a timestamp.")
    return parser.parse_args()

if __name__=="__main__":
    args = parse_args()

    dataset = ShepardMetzler()
    model = GenerativeQueryNetwork()

    model_trainer = ModelTrainer(model)
    model_trainer.train()
