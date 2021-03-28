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

    def single_layer_forward_propagation(A_prev, W_curr, b_curr, activation="relu"):
        # calculation of the input value for the activation function
        Z_curr = np.dot(W_curr, A_prev) + b_curr
        
        # selection of activation function
        if activation is "relu":
            activation_func = relu
        elif activation is "sigmoid":
            activation_func = sigmoid
        else:
            raise Exception('Non-supported activation function')
            
        # return of calculated activation A and the intermediate Z matrix
        return activation_func(Z_curr), Z_curr
