# coding: utf-8

import numpy

# 一维矩阵
vector = numpy.array([5, 10, 15, 20])
equal_to_ten_and_five = (vector == 10) & (vector == 5)
print(equal_to_ten_and_five) # [False False False False]

equal_to_ten_and_five = (vector == 10) | (vector == 5)
print(equal_to_ten_and_five) # [ True  True False False]

equal_to_ten_and_five = (vector == 10) | (vector == 5)
vector[equal_to_ten_and_five] = 50
print(vector) # [50 50 15 20]

matrix = numpy.array([
  [5, 10, 15],
  [20, 25, 30],
  [35, 40, 45]
])

second_column_25 = matrix[:,] == 25
print(second_column_25)
matrix[second_column_25,1] = 10
print(matrix)