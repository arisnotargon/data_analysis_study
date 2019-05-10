from tensorflow.examples.tutorials.mnist import input_data
from scipy import misc as scimsc
import os

if __name__ == '__main__':
    mnist = input_data.read_data_sets('./MNIST_data/', one_hot = True)
    save_dir = './MNIST_data/raw/'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    for idx in range(20):
        image_array = mnist.train.images[idx, :]
        image_array = image_array.reshape(28, 28)

        filename = '%smnist_train_%d.jpg' % (save_dir, idx)

        scimsc.toimage(image_array,cmin = 0.0,cmax = 1.0).save(filename)

    print('finish')
