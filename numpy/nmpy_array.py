# coding: utf-8

import numpy

# 一维矩阵
vector = numpy.array([5, 10, '15', 20.0])

# 二维矩阵
matrix = numpy.array([[2, 4, 8], [20, 25, 30], [40, 45, 48]])
print(vector)
print(matrix)

# 行和列
print(vector.shape)
print(type(vector))

# 2行3列
print(matrix.shape)

one = matrix[1, 1]
print(one) # 25

print(vector[0:3]) # 0, 1, 2 => '5', '10', '15'

# 取某已列
print(matrix[:, 0]) # 2 20 第一列
print(matrix[:, 1]) # 4 24 第二列

equal_to_ten = (vector == '10')
print(equal_to_ten) # [Flase True False False]
print(vector[equal_to_ten]) # '10'


