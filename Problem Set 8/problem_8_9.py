from pylab import *

def g(x):
    return 2*x-3

x = linspace(0,5,num=100)
plot(x,g(x))
xlabel('$x$')
ylabel('$y$')
grid('on')
show()
