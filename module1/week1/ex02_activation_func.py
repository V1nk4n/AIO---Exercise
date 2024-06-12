import math

# Ex2

def is_number(n) :
    try:
        float(n) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    
    return True

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def relu(x):
    if x <= 0:
        return 0
    
    return x

def elu(x):
    alpha = 0.01
    if x <= 0:
        return alpha*(math.exp(x) - 1)
    
    return x 
    
activation_func_dict = {
    "sigmoid": sigmoid,
    "relu": relu,
    "elu": elu
}

def compute_activation_function():
    x = input('input x = ')
    if not is_number(x):
        print('x must be a number')
        return
    x = float(x)

    func_name = input('Input activation Function (sigmoid | relu | elu): ')
    if func_name not in activation_func_dict:
        print(f'{func_name} is not supported')
        return
    
    func = activation_func_dict[func_name]
    value_f = func(x)

    print(f'{func_name}: f({x}) = {value_f}')    
