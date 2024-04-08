import torch 

x = torch.arange(4, dtype=torch.float32).reshape(2,2)
print(x)
# tensor([[0., 1.],
#         [2., 3.]])


print(x.sum())
# tensor(6.)

# 纵向相加
x_sum_0 = x.sum(axis = 0)
print(x_sum_0)
# tensor([2., 4.])

# 横向相加
x_sum_0 = x.sum(axis = 1)
print(x_sum_0)
# tensor([1., 5.])

# ⾏和列对矩阵求和，等价于对矩阵的所有元素进⾏求和
x_sum_all = x.sum(axis=[0, 1]) # x.sum()
print(x_sum_all)
# tensor(6.)

# 元素个数
print(x.numel())

x_mean = x.sum() / x.numel() # 等同于 x.mean()
print(x_mean)
# tensor(1.5000)




# 非降维求和
sum_x = x.sum(axis=1, keepdims=True)
print(sum_x)
# tensor([[1.],
#         [5.]])