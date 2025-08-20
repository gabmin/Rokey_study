import torch

B = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])

print(B.device)


a = torch.tensor([[1], [2], [3]])
b = torch.tensor([4, 5, 6])

print(a + b)


a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

result = torch.cat([a, b], dim=1)
print(result)
