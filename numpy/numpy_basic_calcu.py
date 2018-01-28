import numpy as np

# numpy基础运算
a = np.array([10, 20, 30, 40])
b = np.arange(4)  # [0 1 2 3]
c = a - b  # a中元素逐个减去b中元素
c = a + b
c = b**2#逐个平方
c = np.sin(a)#对a的每一个值求正弦函数
c = np.cos(a)#对a的每一个值求余弦函数

print(c)
print(b<3)#返回各个元素是否小于3
print(b==3)#返回各个元素是否等于3

a = np.array([
    [1,2],
    [3,4]
])
b = np.arange(4).reshape((2,2))
c = a*b#逐个相乘
c_dot = np.dot(b,a)#矩阵乘法,交换参数结果不同
print(c_dot)
c_dot = a.dot(b)#相当于np.dot(a,b)
print(c_dot)

a = np.random.random((2,4))#生成2行4列矩阵,0到1直接随机值
print(a)
print(a.min())#最小值
print('axis:',a.min(axis=0))#1为列中最小,0为行中最小
print(a.max())#最大值
print(a.sum(axis=0))#求和,axis为列中求和,0为行中求和

