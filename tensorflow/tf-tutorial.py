import tensorflow as tf

# Building the computational graph.
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)

# Running the computational graph.
sess = tf.Session()
print(sess.run([node1, node2]))

