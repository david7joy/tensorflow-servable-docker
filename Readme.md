### TENSORFLOW SERVING BASICS 

The key goal of this project is to understand :

1) Create and Save a Tensorflow Model so that it can be loaded to with Tensorflow serving 
model server and use it in a production scenario. 

2) Serve the model with Tensorflow Serving ModelServer.( Using a Docker )

3) Send requests and get responses ( Try a simple integration with Django Web Application Framework)

#### 1. Creating a simple model

`simple_model.py` covers a basic model - which can either add, subtract or 
multiply. The model is very primitive in nature, however, its the same basic
fundamental for more complex models.

#### 2. Save the model

`simple_model.py` also covers how to save a model. 

We could wrap this code in an API endpoint written in a Python framework like Flask, Falcon or similar, and voilá we have an API. 
But there are some really good reasons you don’t want to do it that way:

- If your model(s) are complex and run slowly on CPU, you would want to run your models on more accelerated hardware (like GPUs). Your API-microservice(s), on the other hand, usually run fine on CPU and they’re often running in “everything agnostic” Docker containers. In that case you may want to keep those two kinds of services on different hardware.

- If you start messing up your neat Docker images with heavy TensorFlow models, they grow in every possible direction (CPU usage, memory usage, container image size, and so on). You don’t want that.

- Let’s say your service uses multiple models written in different versions of TensorFlow. Using all those TensorFlow versions in your Python API at the same time is going to be a total mess.

- You could of course wrap one model into one API. Then you would have one service per model and you can run different services on different hardware. Perfect! Except, this is what TensorFlow Serving ModelServer is doing for you. So don’t go wrap an API around your Python code (where you’ve probably imported the entire tf library, tf.contrib, opencv, pandas, numpy, …). TensorFlow Serving ModelServer does that for you.

steps : 

1. `model_input` ,`model_output` :  First we have to grab the input and output tensors.

2. `signature_definition` : Create a signature definition from the input and output tensors. The signature definition is what the model builder use in order to save something a model server can load.
We must give inputs and outputs for signature definition and also `method_name`, this is mandatory without this saving doesn't work. There are 3 kinds of methods such as
predict, classfiy and regress methods. If we don't one of these methods then the saving will give an error.

3. `builder` and `builder.save` : Save the model at a specified path where a server can load it from.

#### 3. Serving the model 



Few Changes made to the process.

- added grpcio to conda using `conda install grpcio`
