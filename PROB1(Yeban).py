import numpy as np 
import matplotlib.pyplot as lib

x = np.arange(0,100)
if x.all() <= 9:
    y= x**2 - 7
else:
    y= x-10
lib.stem(x,y,'--',markerfmt='.')
lib.title('Exponential Increase in graph')
lib.ylabel('Y axis')
lib.xlabel('X axis')
lib.grid()
lib.show()