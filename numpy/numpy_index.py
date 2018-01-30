import numpy as np

sep = lambda :print('<=========================>')

a = np.arange(3, 15)
a = a.reshape(3, 4)  # 重整为3行4列
print(a)
sep()
print(a[1:])  # 打印第1行和之后所有行
sep()
print(a[0, :])  # 打印第0行
sep()
print(a[1, 1])  # 打印1行1列的元素

ind = 0
for row in a:
    print('row ', ind, ':', row)
    ind += 1

sep()
t = a.T  # 矩阵转秩
print('转秩:\n', t)
ind = 0
#转秩之后遍历行相当于迭代原矩阵的列
for col in t:
    print('col', ind, ':', col)
    ind += 1

sep()
print(a.flatten())#恢复成一行
#flat为迭代器对象
for i in a.flat:
    print(i)