import torch

# 当调⽤函数来实例化张量时，我们可以通过指定两个分量m和n来创建⼀个形状为m × n的矩阵
A = torch.arange(20).reshape(5, 4)
print(A)
# tensor([[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11],
#         [12, 13, 14, 15],
#         [16, 17, 18, 19]])

# 访问矩阵的转置
print(A.T)
# tensor([[ 0,  4,  8, 12, 16],
#         [ 1,  5,  9, 13, 17],
#         [ 2,  6, 10, 14, 18],
#         [ 3,  7, 11, 15, 19]])

# 对称矩阵
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)
# tensor([[1, 2, 3],
#         [2, 0, 4],
#         [3, 4, 5]])

print(B == B.T)
# tensor([[True, True, True],
#         [True, True, True],
#         [True, True, True]])