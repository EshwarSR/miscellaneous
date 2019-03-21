import tensorflow as tf

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")

f = x*x*y + y + 2

""" 
The above code does not perform any computation. 
It just creates the variables. 
It DOESNOT even initialize the variables.
"""

"""
Now that the graph is created, we need to 
1. Open a tf session
2. Initialise the parameters
3. Evaluate the f
4. Close the session to free up the space
"""

# 1. Open a tf session
sess = tf.Session()

# 2. Initialise the parameters
sess.run(x.initializer)
sess.run(y.initializer)

# 3. Evaluate the f
result = sess.run(f)
print("result", result)

# 4. Close the session to free up the space
sess.close()


# Faster way of doing

with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    # equivalent to tf.get_default_session().run(x.intializer) type(x.initializer)=Operation (node in graph)

    result = f.eval()
    # equivalent to tf.get_default_session().run(f) and  type(f)=Tensor
    # eval() because we always evaluate a tensor and run() an operation

    print("Result", result)

"""
x.initializer.run()
y.initializer.run()

If there are many variables to be initialized,
init = tf.global_variables_initializer()
with tf.Session() as sess:
    init.run()
    result = f.eval()
"""


"""
Managing graphs

Any node created will be added to the default graph. 

>>> x1 = tf.Variable(1)
>>> x1.graph is tf.get_default_graph()
True

But if we want to add it to a custom graph, we can create a new graph and make it default in a with block.

>>> graph = tf.Graph()
>>> with graph.as_default():
...     x2 = tf.Variable(2)
... 
>>> x2.graph is graph
True
>>> x2.graph is tf.get_default_graph()
False

"""