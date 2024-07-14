import math
import random

#Ex3

def mae(y, y_hat):
    return abs(y - y_hat)

def mse(y, y_hat):
    return (y - y_hat)**2

def rmse(y, y_hat):
    return math.sqrt(mse(y, y_hat))

loss_func_dict = {
    "MAE": mae,
    "MSE": mse,
    "RMSE": rmse
}

def compute_loss_function():
    num_samples = input('Input number of samples ( integer number ) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    num_samples = int(num_samples)

    loss_name = input('Input loss name (MAE | MSE | RMSE): ')
    lost_func = loss_func_dict[loss_name]

    losses = 0
    for sample in range(num_samples):
        y = (random.uniform(0, 10))
        y_hat = (random.uniform(0, 10))
        loss = lost_func(y, y_hat)
        losses += loss
        print(f'loss name: {loss_name}, sample: {sample}, pred: {y_hat}, target: {y}, loss: {loss}')

    final_loss = losses/num_samples
    print(f'final {loss_name}: {final_loss}')