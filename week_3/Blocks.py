import numpy as np

###################################################
# put `dense_forward` and `dense_grad_input` here #
###################################################


###################################################
#   put `dense_grad_W` and `dense_grad_b` here    #
###################################################


###################################################
# put `relu_forward` and `relu_grad_input` here   #
###################################################


###################################################
# put `hinge_forward` and `hinge_grad_input` here #
###################################################


###################################################
#        put `l2_regularizer`  here               #
###################################################


###################################################
#        put here whatever you want               #
###################################################


class Layer(object):
    
    def __init__(self):
        self.training_phase = True
        self.output = 0.0
        
    def forward(self, x_input):
        self.output = x_input
        return self.output
    
    def backward(self, x_input, grad_output):
        return grad_output
    
    def get_params(self):
        return []
    
    def get_params_gradients(self):
        return []



class Dense(Layer):
    
    def __init__(self, n_input, n_output):
        super(Dense, self).__init__()
        #Randomly initializing the weights from normal distribution
        self.W = np.random.normal(size=(n_input, n_output))
        self.grad_W = np.zeros_like(self.W)
        #initializing the bias with zero
        self.b = np.zeros(n_output)
        self.grad_b = np.zeros_like(self.b)
      
    def forward(self, x_input):
        self.output = dense_forward(x_input, self.W, self.b)
        return self.output
    
    def backward(self, x_input, grad_output):
        # get gradients of weights
        self.grad_W = dense_grad_W(x_input, grad_output, self.W, self.b)
        self.grad_b = dense_grad_b(x_input, grad_output, self.W, self.b)
        # propagate the gradient backwards
        return dense_grad_input(x_input, grad_output, self.W, self.b)
    
    def get_params(self):
        return [self.W, self.b]

    def get_params_gradients(self):
        return [self.grad_W, self.grad_b]



class ReLU(Layer):
        
    def forward(self, x_input):
        self.output = relu_forward(x_input)
        return self.output
    
    def backward(self, x_input, grad_output):
        return relu_grad_input(x_input, grad_output)



class SequentialNN(object):

    def __init__(self):
        self.layers = []
        self.training_phase = True
        
    def set_training_phase(is_training=True):
        self.training_phase = is_training
        for layer in self.layers:
            layer.training_phase = is_training
        
    def add(self, layer):
        self.layers.append(layer)
        
    def forward(self, x_input):
        self.output = x_input
        for layer in self.layers:
            self.output = layer.forward(self.output)
        return self.output
    
    def backward(self, x_input, grad_output):
        inputs = [x_input] + [l.output for l in self.layers[:-1]]
        for input_, layer_ in zip(inputs[::-1], self.layers[::-1]):
            grad_output = layer_.backward(input_, grad_output)
            
    def get_params(self):
        params = []
        for layer in self.layers:
            params.extend(layer.get_params())
        return params
    
    def get_params_gradients(self):
        grads = []
        for layer in self.layers:
            grads.extend(layer.get_params_gradients())
        return grads



class Loss(object):
    
    def __init__(self):
        self.output = 0.0
        
    def forward(self, target_pred, target_true):
        return self.output
    
    def backward(self, target_pred, target_true):
        return np.zeros_like(target_pred)



class Hinge(Loss):
    
    def forward(self, target_pred, target_true):
        self.output = hinge_forward(target_pred, target_true)
        return self.output
    
    def backward(self, target_pred, target_true):
        return hinge_grad_input(target_pred, target_true)



class Optimizer(object):
    '''This is a basic class. 
    All other optimizers will inherit it
    '''
    def __init__(self, model, lr=0.01, weight_decay=0.0):
        self.model = model
        self.lr = lr
        self.weight_decay = weight_decay
        
    def update_params(self):
        pass



class SGD(Optimizer):
    '''Stochastic gradient descent optimizer
    https://en.wikipedia.org/wiki/Stochastic_gradient_descent
    '''
        
    def update_params(self):
        weights = self.model.get_params()
        grads = self.model.get_params_gradients()
        for w, dw in zip(weights, grads):
            update = self.lr * dw + self.weight_decay * w
            # it writes the result to the previous variable instead of copying
            np.subtract(w, update, out=w) 




