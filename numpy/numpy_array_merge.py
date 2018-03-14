import numpy as np

aArr = np.array([1, 1, 1])
bArr = np.array([2, 2, 2])
cArr = np.vstack((aArr, bArr))  # 上下合并
dArr = np.hstack((aArr, bArr))  # 左右合并
print(dArr)

eArr = aArr[:,np.newaxis]#增加维度,变成一列数据
print(eArr)
eArr = aArr[np.newaxis,:]#增加维度,原数组成为新的表第一个行
print(eArr)

#多个合并的写法
A = aArr[:,np.newaxis]
B = bArr[:,np.newaxis]
eArr = np.concatenate((A,B,B,A),axis=0)#axis参数是合并的维度,小于等于输入数组的维度
print(eArr)