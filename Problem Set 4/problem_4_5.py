from pylab import *
 
def f(x):
    return -3*sin(x)/x + 4
 
x = linspace(0.1,100,num=1000)
plot(x,f(x))
show()