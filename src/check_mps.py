import torch

device = "mps" if torch.backends.mps.is_available() else "cpu"

x = torch.rand(size=(3,4)).to(device)
print (x)