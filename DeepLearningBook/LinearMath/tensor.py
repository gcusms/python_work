import torch


A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()
# 通过分配新内存，将A的⼀个副本分配给B
print(A)
# tensor([[ 0.,  1.,  2.,  3.],
#         [ 4.,  5.,  6.,  7.],
#         [ 8.,  9., 10., 11.],
#         [12., 13., 14., 15.],
#         [16., 17., 18., 19.]])

print(A + B)
# tensor([[ 0.,  2.,  4.,  6.],
#         [ 8., 10., 12., 14.],
#         [16., 18., 20., 22.],
#         [24., 26., 28., 30.],
#         [32., 34., 36., 38.]])

print(A * B)
# tensor([[  0.,   1.,   4.,   9.],
#         [ 16.,  25.,  36.,  49.],
#         [ 64.,  81., 100., 121.],
#         [144., 169., 196., 225.],
#         [256., 289., 324., 361.]])

a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(a + X)
# tensor([[[ 2,  3,  4,  5],
#          [ 6,  7,  8,  9],
#          [10, 11, 12, 13]],

#         [[14, 15, 16, 17],
#          [18, 19, 20, 21],
#          [22, 23, 24, 25]]])
  
print((a * X).shape)
# torch.Size([2, 3, 4])