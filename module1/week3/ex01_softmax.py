import torch
from torch.nn import Module
import torch.nn as nn
import math


class Softmax(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        total_exp_x = sum(exp_x)
        return exp_x/total_exp_x


class softmax_stable(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = max(x)
        exp_x = torch.exp(x-c)
        total_exp_x = sum(exp_x)
        return exp_x/total_exp_x


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
softmax_function = softmax_stable()
output = softmax_function(data)
print(output)

