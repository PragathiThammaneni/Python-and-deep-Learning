import tensorflow as tf # imported the tensor flow package
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
session = tf.Session() # created a session and 3 matrices
A = tf.constant([1,5,3,2],shape=[2,2])
B = tf.constant([1,7,4,2],shape=[2,2])
C = tf.constant([3,4,5,9],shape=[2,2])
# function (a^2+b)*c and a, b, and c should be the matrices
D = tf.pow(A,2)
E = tf.add(D,B)
F = tf.multiply(E,C)
# Printing the output generated
print(session.run(F))