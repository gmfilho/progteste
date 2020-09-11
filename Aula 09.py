'''
import numpy as np

vetor = np.array(((1., 0., 0.),(0.,1.,2.)), dtype=complex)
print(vetor)


import numpy as np
print(np.zeros((3,4)))
print(np.ones((2,3,4), dtype = np.int16))
print(np.empty((2,3)))
print(np.arange(10,30,5))
print(np.arange(0,2,0.3),'\n')
print(np.random.random(15))
print(np.random.random(15).reshape(3,5))


import numpy as np 
from numpy import pi

#x = np.linspace(0,2,9)
x = np.linspace(0,2*pi,100)
f = np.sin(x)
print(x)
print(f)

import numpy as np 
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)

c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)
print(a-35)
print(35-a)


import numpy as np 

A = np.array([[1,1],
             [0,1]])
B = np.array([[2,0],
              [3,4]])

print(A)
print(B)
print(A*B)
print(A-B)
print(A+B)
print(A@B)
print(A.dot(B))


import numpy as np 

a = np.ones((2,3), dtype = int)
b = np.random.random((2,3))
print(a);print(b)
a *= 3
print(a)


'''