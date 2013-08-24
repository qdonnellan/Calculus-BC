from pylab import *

def f(x):
  return x**2

x = linspace(0,2,num=1000)
plot(x,f(x))
plot(1,f(1),'wo')
plot(1,2, 'bo')
show()