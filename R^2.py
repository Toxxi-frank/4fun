import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced
    # predictions.
    #
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    y_mean = np.mean(data)
    r_squared = 1 - np.sum(np.square(data - predictions))/np.sum(np.square(data - y_mean))

# SST = ((data - np.mean(data)**2)).sum()
# SSReg = ((data - predictions)**2)).sum()
    # r_squared = 1 - SSReg/SST

    return r_squared