import torch

# ⾏向量 x_arange
x_arang = torch.arange(12)
print(x_arang)
# tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

# 张量（沿每个轴的⻓度）的形状  torch.Size([12])
print(x_arang.shape) 

# 元素的总数 12
print(x_arang.numel())

# 改变⼀个张量的形状⽽不改变元素数量和元素值
X_arange  = x_arang.reshape(3,4)

print(X_arange)
# tensor([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])

# 全0
x_zeros = torch.zeros((2, 3, 4))
print(x_zeros)
# tensor([[[0., 0., 0., 0.],
#          [0., 0., 0., 0.],
#          [0., 0., 0., 0.]],

#         [[0., 0., 0., 0.],
#          [0., 0., 0., 0.],
#          [0., 0., 0., 0.]]])

# 全0
x_ones = torch.ones((2, 3, 4))
print(x_ones)
# tensor([[[1., 1., 1., 1.],
#          [1., 1., 1., 1.],
#          [1., 1., 1., 1.]],

#         [[1., 1., 1., 1.],
#          [1., 1., 1., 1.],
#          [1., 1., 1., 1.]]])



# 每个元素都从均值为0、标准差为1的标准⾼斯分布（正态分布）中随机采样
x_randn = torch.randn(3, 4)
print(x_randn)
#tensor([[-0.0280,  1.2447,  0.4057, -0.3677],
#       [-0.2967,  0.5702,  0.4615,  1.3417],
#       [-1.5241, -1.4811,  2.2914, -1.0492]])


## 运算符
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y)  # tensor([ 3.,  4.,  6., 10.])
print(x - y)  # tensor([-1.,  0.,  2.,  6.])
print(x * y)  # tensor([ 2.,  4.,  8., 16.])
print(x / y)  # tensor([0.5000, 1.0000, 2.0000, 4.0000])
print(x ** y)  # tensor([ 1.,  4., 16., 64.]) **运算符是求幂运算


# 把多个张量连结（concatenate）在⼀起
# 第⼀个输出张量的dim = 0⻓度（6）是两个输⼊张量轴-0⻓度的总和（3 + 3）；
# 第⼆个输出张量的dim = 1⻓度（8）是两个输⼊张量轴-1⻓度的总和（4 + 4
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0))
# tensor([[ 0.,  1.,  2.,  3.],
#         [ 4.,  5.,  6.,  7.],
#         [ 8.,  9., 10., 11.],
#         [ 2.,  1.,  4.,  3.],
#         [ 1.,  2.,  3.,  4.],
#         [ 4.,  3.,  2.,  1.]])

print(torch.cat((X, Y), dim=1))
# tensor([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
#         [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
#         [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]])

# 若位置的元素相等则X == Y在该位置处为真，否则该位置为0 
print(X == Y)
# tensor([[False,  True, False,  True],
#         [False, False, False, False],
#         [False, False, False, False]])


# 将⼤⼩为1的张量转换为Python标量，我们可以调⽤item函数或Python的内置函数
a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a))
# tensor([3.5000]) 3.5 3.5 3