import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy
from scipy import misc

if __name__ == '__main__':
    mnist = input_data.read_data_sets('./MNIST_data/', one_hot = True)
    # print(mnist.train.images.shape)
    # print(mnist.train.labels.shape)
    # print(mnist.validation.images.shape)
    # print(mnist.validation.labels.shape)
    # print(mnist.test.images.shape)
    # print(mnist.test.labels.shape)

    # numpy的多维数组切片,维度间用逗号隔开
    # print(mnist.train.images[0, :])

    # 独热表示(one hot),类似于子网掩码,在哪一位就是哪个标签,例如[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]是7
    print(mnist.train.labels[0, :])
    for i in range(20):
        one_hot_lable = mnist.train.labels[i]
        # numpy.argmax()返回数组最大值的下标
        label = numpy.argmax(one_hot_lable)
        print(label)

    ''' softman函数,利用分值计算概率,自然数e,事件A,B,C的分值为a,b,c,事件A的概率为(e^a)/(e^a + e^b + e^c)
    各事件概率加和为1:(e^a)/(e^a + e^b + e^c) + (e^b)/(e^a + e^b + e^c) + (e^c)/(e^a + e^b + e^c) = 1
    '''
