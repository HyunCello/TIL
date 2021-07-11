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

# 6 ############
# ft = torch.Tensor([0, 1, 2])
# print(ft.shape)

# print(ft.unsqueeze(0))
# print(ft.unsqueeze(0).shape)

# print(ft.view(1, -1))
# print(ft.view(1, -1).shape)

# print(ft.unsqueeze(1))
# print(ft.unsqueeze(1).shape)

# print(ft.unsqueeze(-1))
# print(ft.unsqueeze(-1).shape)

# 7 ##################

# lt = torch.LongTensor([1, 2, 3, 4])
# print(lt)

# print(lt.float())

# bt = torch.ByteTensor([True, False, False, True])
# print(bt)

# print(bt.long())
# print(bt.float())

# 8 ########################
# x = torch.FloatTensor([[1, 2], [3, 4]])
# y = torch.FloatTensor([[5, 6], [7, 8]])

# print(torch.cat([x, y], dim = 0))
# print(torch.cat([x, y], dim = 1))


# 9 ########################
# x = torch.FloatTensor([1, 4])
# y = torch.FloatTensor([2, 5])
# z = torch.FloatTensor([3, 6])

# print(torch.stack([x, y, z]))

# print(torch.cat([x.unsqueeze(0), y.unsqueeze(0), z.unsqueeze(0)], dim = 0))

# print(torch.stack([x, y, z], dim = 1))


# 10 #######################
# x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
# print(x)
# print(torch.ones_like(x))
# print(torch.zeros_like(x))


# 11 ###############
x = torch.FloatTensor([[1, 2], [3, 4]])
# print(x.mul(2.))
# print(x)
print(x.mul_(2.))
print(x)