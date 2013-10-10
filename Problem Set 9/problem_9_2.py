from pylab import *

def f(x):
    return 2+0*x
    
def g(x):
    return x

def h(x):
    return x+2

x = linspace(0,2,num=10)
plot(x,f(x), 'b-')

x = linspace(2,4,num=10)
plot(x,g(x),'b-')

x = linspace(-2,0,num=10)
plot(x,h(x), 'b-')

xlabel('$x$')
ylabel("$f'(x)$")
title("Graph of $f'$")
grid('on')

show()