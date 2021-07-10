import numpy as np
import torch


t = np.array([[[0, 1, 2],
               [3, 4, 5]],
              [[6, 7, 8],
               [9, 10, 11]]])
ft = torch.FloatTensor(t)

# print(ft.shape)

# print(ft.view([-1, 3]))
# print(ft.view([-1, 3]).shape)

# print(ft.view([-1, 1, 3]))
# print(ft.view([-1, 1, 3]).shape)

########################
# ft = torch.FloatTensor([[0], [1], [2]])
# print(ft)
# print(ft.shape)

# print(ft.squeeze())
# print(ft.squeeze().shape)

########################
ft = torch.Tensor([0, 1, 2])
print(ft.shape)

# print(ft.unsqueeze(0))
# print(ft.unsqueeze(0).shape)

# print(ft.view(1, -1))
# print(ft.view(1, -1).shape)

# print(ft.unsqueeze(1))
# print(ft.unsqueeze(1).shape)

print(ft.unsqueeze(-1))
print(ft.unsqueeze(-1).shape)