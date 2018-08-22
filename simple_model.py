import tensorflow as tf
from tensorflow.python.saved_model.utils import build_tensor_info
from tensorflow.python.saved_model import signature_def_utils
from tensorflow.python.saved_model import signature_constants
from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model import builder as saved_model_builder

# Declaring placeholder and other variables
a = tf.placeholder(tf.int32,name='a')
b = tf.constant(10)

# Our Model
subtract = tf.subtract(a,b,name='subtract')
# print(a) to get input tensor a:0 and print(add) to get output tensor add:0

with tf.Session() as sess:
    # Few operations
    ten_plus_two = sess.run(subtract,feed_dict={a:2})
    print('10+2 = {}'.format(ten_plus_two))

    ten_plus_seven = sess.run(subtract,feed_dict={a:7})
    print('10+7 = {}'.format(ten_plus_seven))

# Pick picking out the model input and output
a_tensor = sess.graph.get_tensor_by_name('a:0')
sum_tensor = sess.graph.get_tensor_by_name('subtract:0')

model_input = build_tensor_info(a_tensor)
model_output = build_tensor_info(sum_tensor)

# Creating a model signature for using during tf Serving
signature_definition = signature_def_utils.build_signature_def(inputs={'inputs':model_input},
                                                               outputs={'outputs':model_output},
                                                               method_name=signature_constants.PREDICT_METHOD_NAME)

# These constants are defined in signature_constants.py, and there are three sets of constants:
# predictions, classification and regression.

# saving the model
builder = saved_model_builder.SavedModelBuilder('./models/simple_model_subtract/1')

builder.add_meta_graph_and_variables(sess, [tag_constants.SERVING],
                                     signature_def_map={signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:signature_definition})

builder.save()



