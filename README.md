# MNIST-From-Scratch
Classifying the MNIST handwritten digit dataset using only numpy.

### The MNIST Dataset

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/MnistExamples.png/320px-MnistExamples.png)

#### The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. This is also called the "Hello World" of machine learning. The MNIST database contains 60,000 training images and 10,000 testing images. Half of the training set and half of the test set were taken from NIST's training dataset, while the other half of the training set and the other half of the test set were taken from NIST's testing dataset. The digits were written by high school students and employees of the United States Census Bureau.

# The logic and concepts of working:

### Neural networks.

#### The basic idea behind a neural network is to simulate (copy in a simplified but reasonably faithful way) lots of densely interconnected brain cells inside a computer so you can get it to learn things, recognize patterns, and make decisions in a humanlike way. The amazing thing about a neural network is that you don't have to program it to learn explicitly: it learns all by itself, just like a brain (Not really but yeah)!

### What does a neural network consist of?

![image](https://databricks.com/wp-content/uploads/2019/02/neural1.jpg)

#### A typical neural network has anything from a few dozen to hundreds, thousands, or even millions of artificial neurons called units arranged in a series of layers, each of which connects to the layers on either side. The first layer or the Input layer are designed to receive various forms of information from the outside world that the network will attempt to learn about, recognize. Other units sit on the opposite side of the network and signal how it responds to the information it's learned; those are known as output units. In between the input units and output units are one or more layers of hidden units, which, together, form the majority of the artificial brain.Most neural networks are fully connected, which means each hidden unit and each output unit is connected to every unit in the layers either side. 

#### The connections between one unit and another are represented by a number called a weight, which can be either positive (if one unit excites another) or negative (if one unit suppresses or inhibits another).Each neuros has a bias aswell, you can think of the bias as a measure of how easy it is to get a node to fire. For a node with a large bias, the output will tend to be intrinsically high, with small positive weights and inputs producing large positive outputs (near to 1). Biases can be also negative, leading to sigmoid outputs near to 0. If the bias is very small (or 0), the output will be decided by the values of weights and inputs alone. Further reading [ANN](https://en.wikipedia.org/wiki/Artificial_neural_network), [Artificial neurons](https://en.wikipedia.org/wiki/Artificial_neurons)

### How a neural network learns?


### A little maths about neural networks.

![image](https://miro.medium.com/max/1400/1*6Kn68RFH0QMQ7gPSpulh0A.png)

#### For each input, multiply the input value xᵢ with weights wᵢ and sum all the multiplied values. Weights — represent the strength of the connection between neurons and decides how much influence the given input will have on the neuron’s output. If the weight w₁ has a higher value than the weight w₂, then the input x₁ will have a higher influence on the output than w₂.
