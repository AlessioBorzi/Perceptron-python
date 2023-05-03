import numpy
import pandas

def perceptron(csv_file, T):  
    for t in range(T):
        data = pandas.read_csv(csv_file)
        d = data.shape[1]-1 # space dimension
        n = data.shape[0] # number of points
        theta = numpy.zeros(d)
        for i in range(n):
            x = data.iloc[i, 0:d]
            y = data.iloc[i, d]
            if y * numpy.dot(x, theta) <= 0:
                theta += y*x
    return theta
