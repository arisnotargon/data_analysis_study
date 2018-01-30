import numpy as np

aArr = np.array([1, 1, 1])
bArr = np.array([2, 2, 2])
cArr = np.vstack((aArr, bArr))  # 上下合并
dArr = np.hstack((aArr, bArr))  # 左右合并
print(dArr)
