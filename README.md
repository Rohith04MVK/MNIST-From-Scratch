# MNIST-From-Scratch
#### Classifying the MNIST handwritten digit dataset using only numpy.


### The MNIST Dataset

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/MnistExamples.png/320px-MnistExamples.png)

#### The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. This is also called the "Hello World" of machine learning. The MNIST database contains 60,000 training images and 10,000 testing images. Half of the training set and half of the test set were taken from NIST's training dataset, while the other half of the training set and the other half of the test set were taken from NIST's testing dataset. The digits were written by high school students and employees of the United States Census Bureau.

# The logic and concepts of working:

### Neural networks.

The basic idea behind a neural network is to simulate (copy in a simplified but reasonably faithful way) lots of densely interconnected brain cells inside a computer so you can get it to learn things, recognize patterns, and make decisions in a humanlike way. The amazing thing about a neural network is that you don't have to program it to learn explicitly: it learns all by itself, just like a brain (Not really but yeah)!

### What does a neural network consist of?

![image](https://databricks.com/wp-content/uploads/2019/02/neural1.jpg)

A typical neural network has anything from a few dozen to hundreds, thousands, or even millions of artificial neurons called units arranged in a series of layers, each of which connects to the layers on either side. The first layer or the Input layer are designed to receive various forms of information from the outside world that the network will attempt to learn about, recognize. Other units sit on the opposite side of the network and signal how it responds to the information it's learned; those are known as output units. In between the input units and output units are one or more layers of hidden units, which, together, form the majority of the artificial brain.Most neural networks are fully connected, which means each hidden unit and each output unit is connected to every unit in the layers either side. 

The connections between one unit and another are represented by a number called a weight, which can be either positive (if one unit excites another) or negative (if one unit suppresses or inhibits another).Each neuros has a bias aswell, you can think of the bias as a measure of how easy it is to get a node to fire. For a node with a large bias, the output will tend to be intrinsically high, with small positive weights and inputs producing large positive outputs (near to 1). Biases can be also negative, leading to sigmoid outputs near to 0. If the bias is very small (or 0), the output will be decided by the values of weights and inputs alone. Further reading [ANN](https://en.wikipedia.org/wiki/Artificial_neural_network), [Artificial neurons](https://en.wikipedia.org/wiki/Artificial_neurons)

### How a neural network learns?

Information flows through a neural network in two ways. When it's learning (being trained) or operating normally (after being trained), patterns of information are fed into the network via the input units, which trigger the layers of hidden units, and these in turn arrive at the output units. This common design is called a feedforward network. Not all units "fire" all the time. Each unit receives inputs from the units to its left, and the inputs are multiplied by the weights of the connections they travel along. Every unit adds up all the inputs it receives in this way and (in the simplest type of network) if the sum is more than a certain threshold value aka the bias, the unit "fires" and triggers the units it's connected to (those on its right).

For a neural network to learn, there has to be an element of feedback involved—just as children learn by being told what they're doing right or wrong. In fact, we all use feedback, all the time. Think back to when you first learned to play a game like Rock Paper Scissors. As you played for the first time, your brain watched how the opponent was making moves and tried to recognize a pattern in it. Next time it was your turn, you remembered what you'd done wrong before, modified your moves accordingly, and hopefully played a bit better.So you used feedback to compare the outcome you wanted with what actually happened, figured out the difference between the two, and used that to change what you did next time ("He shows paper a rock" "he shows scissors rearly" and so on). The bigger the difference between the intended and actual outcome, the more radically you would have altered your moves.

Neural networks learn things in exactly the same way, typically by a feedback process called backpropagation. This involves comparing the output a network produces with the output it was meant to produce, and using the difference between them to modify the weights of the connections between the units in the network, working from the output units through the hidden units to the input units—going backward, in other words. In time, backpropagation causes the network to learn, reducing the difference between actual and intended output to the point where the two exactly coincide, so the network figures things out exactly as it should.

### Activations

ReLU - Traditionally, some prevalent non-linear activation functions, like sigmoid functions (or logistic) and hyperbolic tangent, are used in neural networks to get activation values corresponding to each neuron. Recently, the ReLu function has been used instead to calculate the activation values in traditional neural network or deep neural network paradigms. The reasons of replacing sigmoid because the ReLu function is able to accelerate the training speed of deep neural networks compared to traditional activation functions since the derivative of ReLu is 1 for a positive input. Due to a constant, deep neural networks do not need to take additional time for computing error terms during training phase.
<p align="center"><img src="https://ailephant.com/wp-content/uploads/2018/08/ReLU-function-graph-300x234.png"><p>

Sigmoid - The main reason why we use sigmoid function is because it exists between (0 to 1). Therefore, it is especially used for models where we have to predict the probability as an output.Since probability of anything exists only between the range of 0 and 1, sigmoid is the right choice. The function is differentiable.That means, we can find the slope of the sigmoid curve at any two points. The function is monotonic but function’s derivative is not. The logistic sigmoid function can cause a neural network to get stuck at the training time. The softmax function is a more generalized logistic activation function which is used for multiclass classification.

<p align="center"><img src="https://th.bing.com/th/id/R1cc898b08e1abb1fc9d3494b19a28595?rik=lxbci3%2bOLVTF4g&riu=http%3a%2f%2f1.bp.blogspot.com%2f_Tndn7IbKcao%2fSyu0vkRlGtI%2fAAAAAAAAAIk%2fTQ-K2fOr9w0%2fs400%2fSigmoidPlot1.png&ehk=%2b3e3aUWb19M3iolTWTGaLwOeAQCrIOa97BLTuavF%2bwg%3d&risl=&pid=ImgRaw"><p>
