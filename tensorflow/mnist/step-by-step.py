# ran, data downloaded, comment out
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])

# weights and biases
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# model
y = tf.nn.softmax(tf.matmul(x, W) + b)

# correct answers placeholder
y_ = tf.placeholder(tf.float32, [None, 10])

# cross entropy function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# train 
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

# launch
sess = tf.InteractiveSession()

# init
tf.global_variables_initializer().run()

# train
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# check
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# result 
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))



