import tensorflow as tf


def tf11():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))


def tf12():
    a = tf.constant(10)
    b = tf.constant(32)
    sess = tf.Session()
    print(sess.run(a + b))
