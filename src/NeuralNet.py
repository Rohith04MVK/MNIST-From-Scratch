import numpy as np

class NN:
    def __init__(self, shape, neuron, layers):
        self.shape = shape
        self.neuron = neuron
        self.layers = layers

    def init_layers(nn_architecture, seed = 99):
        # random seed initiation
        np.random.seed(seed)
        # number of layers in our neural network
        number_of_layers = len(nn_architecture)
        # parameters storage initiation
        params_values = {}
        
        # iteration over network layers
        for idx, layer in enumerate(nn_architecture):
            # we number network layers from 1
            layer_idx = idx + 1
            
            # extracting the number of units in layers
            layer_input_size = layer["input_dim"]
            layer_output_size = layer["output_dim"]

            
    def sigmoid(Z):
        return 1/(1+np.exp(-Z))

    def relu(Z):
        return np.maximum(0,Z)

    def sigmoid_backward(dA, Z):
        sig = sigmoid(Z)
        return dA * sig * (1 - sig)

    def relu_backward(dA, Z):
        dZ = np.array(dA, copy = True)
        dZ[Z <= 0] = 0
        return dZ


