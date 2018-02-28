# (tensorflow)$ python   用 Python API 写 TensorFlow 示例代码

import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def tf21():
    # 用 NumPy 随机生成 100 个数据
    x_data = np.float32(np.random.rand(2, 100))
    y_data = np.dot([0.100, 0.200], x_data) + 0.300

    # 构造一个线性模型
    b = tf.Variable(tf.zeros([1]))
    w = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
    y = tf.matmul(w, x_data) + b

    # 最小化方差
    loss = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    # 初始化变量
    init = tf.global_variables_initializer()

    # 启动图 (graph)
    sess = tf.Session()
    sess.run(init)

    # 拟合平面
    for step in range(0, 201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(w), sess.run(b))

    sess.close()


def tf22():
    # 创建一个 常量 op, 返回值 'matrix1' 代表这个 1x2 矩阵.
    matrix1 = tf.constant([[3., 3.]])

    # 创建另外一个 常量 op, 返回值 'matrix2' 代表这个 2x1 矩阵.
    matrix2 = tf.constant([[2.], [2.]])

    # 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
    # 返回值 'product' 代表矩阵乘法的结果.
    product = tf.matmul(matrix1, matrix2)

    # 启动图 (graph)
    sess = tf.Session()
    print(sess.run(product))

    sess.close()


def tf23():
    sess = tf.InteractiveSession()

    x = tf.Variable([1.0, 2.0])
    a = tf.constant([3.0, 3.0])

    # 使用初始化器 initializer op 的 run() 方法初始化 'x'
    x.initializer.run()

    # 增加一个减法 sub op, 从 'x' 减去 'a'. 运行减法 op, 输出结果
    sub = tf.subtract(x, a)
    print(sub.eval())

