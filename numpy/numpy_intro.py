import numpy as np
# numpy是基于矩阵的
arr = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]
#使用列表定义numpy的矩阵
arr = np.array(arr)
print(arr)
print(arr.ndim) #维度
print(arr.shape)#行数列数
print(arr.size)#总元素个数