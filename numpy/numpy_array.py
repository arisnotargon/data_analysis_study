import numpy as np
#创建各种numpy的array
a = np.array([2,3,4,5,6,6,7],dtype=np.int)#dtype参数定义类型,不写默认int64
print(a.dtype)#默认为int64
f = np.array([2,3,4,5,6,6,7],dtype=np.float)
print(f.dtype)#默认float64
arr = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])
z = np.zeros((3,4))#生成3行4列全0的矩阵,默认dtype为float64
o = np.ones((3,4),dtype=np.int32)#生成3行4列全1的矩阵,手动设置dtype为int32
e = np.empty((3,4))#生成一个3行4列全部非常接近0的矩阵,默认float
a = np.arange(1,20,2)#生成1到19步进为2的numpy数列
reshape = np.arange(12).reshape((3,4))#将生成的数列重整为指定长宽的矩阵
l = np.linspace(1,10,6)#生成线段1到10,分成6段
l = l.reshape((2,3))#同样可以重整
print(l)