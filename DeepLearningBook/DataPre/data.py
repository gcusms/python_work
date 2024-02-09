import os
import pandas as pd


os.makedirs(os.path.join('./', 'data'), exist_ok=True)
data_file = os.path.join('./', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
  f.write('NumRooms,Alley,Price\n') # 列名
  f.write('NA,Pave,127500\n') # 每⾏表⽰⼀个数据样本
  f.write('2,NA,106000\n')
  f.write('4,NA,178100\n')
  f.write('NA,NA,140000\n')

data = pd.read_csv(data_file)
print(data)
#    NumRooms Alley   Price
# 0       NaN  Pave  127500
# 1       2.0   NaN  106000
# 2       4.0   NaN  178100
# 3       NaN   NaN  140000

# 处理缺失值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
print(inputs)
#    NumRooms Alley
# 0       3.0  Pave
# 1       2.0   NaN
# 2       4.0   NaN
# 3       3.0   NaN

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
#    NumRooms  Alley_Pave  Alley_nan
# 0       3.0           1          0
# 1       2.0           0          1
# 2       4.0           0          1
# 3       3.0           0          1

# 转换为张量模式
import torch
x_input, y_input = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(x_input, y_input)
# tensor([[3., 1., 0.],
#         [2., 0., 1.],
#         [4., 0., 1.],
#         [3., 0., 1.]], dtype=torch.float64) tensor([127500, 106000, 178100, 140000])


