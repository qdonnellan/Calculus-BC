from __future__ import division
from pylab import *

def f(x):
    return sin(x)/x

x = linspace(-2,2,num=1000)
plot(x,f(x))
show()