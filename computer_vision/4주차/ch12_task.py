import torch

X = torch.tensor([1.0, 2.0, 3.0])
epsilon = 0.01
gamma = 2.0
beta = 1.0

mean = X.mean()
var = X.var(unbiased=False)

x_hat = (X - mean) / torch.sqrt(var + epsilon)

Y = gamma * x_hat + beta