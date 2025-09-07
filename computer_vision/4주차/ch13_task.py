import torch
import torch.nn as nn
import torchvision.models as models

model = models.googlenet(pretrained=True)

model.fc = nn.Linear(in_features=4096, out_features=5)

print(model.fc)