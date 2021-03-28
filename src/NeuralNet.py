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
            
            # initiating the values of the W matrix
            # and vector b for subsequent layers
            params_values['W' + str(layer_idx)] = np.random.randn(
                layer_output_size, layer_input_size) * 0.1
            params_values['b' + str(layer_idx)] = np.random.randn(
                layer_output_size, 1) * 0.1
        
    return params_values
            
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

    
    def full_forward_propagation(X, params_values, nn_architecture):
    # creating a temporary memory to store the information needed for a backward step
    memory = {}
    # X vector is the activation for layer 0 
    A_curr = X
    
    # iteration over network layers
    for idx, layer in enumerate(nn_architecture):
        # we number network layers from 1
        layer_idx = idx + 1
        # transfer the activation from the previous iteration
        A_prev = A_curr
        
        # extraction of the activation function for the current layer
        activ_function_curr = layer["activation"]
        # extraction of W for the current layer
        W_curr = params_values["W" + str(layer_idx)]
        # extraction of b for the current layer
        b_curr = params_values["b" + str(layer_idx)]
        # calculation of activation for the current layer
        A_curr, Z_curr = single_layer_forward_propagation(A_prev, W_curr, b_curr, activ_function_curr)
        
        # saving calculated values in the memory
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr
       
    # return of prediction vector and a dictionary containing intermediate values
    return A_curr, memory