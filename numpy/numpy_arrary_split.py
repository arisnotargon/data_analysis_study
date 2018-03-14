import numpy as np

#分割数组,横向纵向
A= np.arange(12).reshape((3,4))
print(A)
#split等量分割,分成相等的多个array
B= np.split(A,4,axis=1)#要分的array,分成的份数,分割维度(1横向,0纵向)
print(B)
#array_split不等分割
C= np.array_split(A,3,axis=1)#第一个array包含2列,另外两个只有1列数据
print(C)

D = np.vsplit(A,3)#纵向分割成3块
D = np.hsplit(A,2)#横向分2块

print(D)