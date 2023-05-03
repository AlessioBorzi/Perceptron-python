import numpy
import pandas

#def perceptron(csv_file, t):
    
data = pandas.read_csv("data.csv")
d = data.shape[1]-1 # space dimension
n = data.shape[0] # number of points
theta = numpy.zeros(d)
for i in range(n):
    r = 

        