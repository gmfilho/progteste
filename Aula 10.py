'''
import numpy as np 

a = np.arange(12)**2
print(a)
j = np.array([[3,4],[9,7]])
print(a[j])


import numpy as np

palette = np.array([[0  ,   0,   0], #preto
                    [255,   0,   0], #vermelho 
                    [  0, 255,   0], #verde
                    [  0,   0, 255], #azul 
                    [255, 255, 255]]) #branco

image = np.array([[0,1,2,0],[0,3,4,0]])
print(palette[image])

import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
i = np.array([[0,1],
              [1,2]])
j = np.array([[2,1],
              [3,3]])
print(a[i,j])

print(a[i,2])
print(a[2,j])
print(a[:,j])
print(a[i,:])


import numpy as np
a = np.arange(12).reshape(3,4)
b = a > 4
print(b)
print(a[b])
print(a[a < 4])

b1 = np.array([False, True, True])
b2 = np.array([True, False, True, False])
print(a[b1,b2])


import numpy as np 
a = np.array([[1.0,2.0], [3.0,4.0]])
print(a)
print(a.transpose())
print(np.linalg.inv(a))
print(np.linalg.det(a))
u = np.eye(2)
print(u)
print(a@a)
print(np.trace(a))
y = np.array([[5.],[7.]])
print(np.linalg.solve(a,y))
print(np.linalg.eig(a))



import matplotlib 
import matplotlib.pyplot as plt
import numpy as np 

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2* np.pi * t)

fig, ax = plt.subplots()
ax.plot(t,s)
plt.show()

import matplotlib.pyplot as plt
import numpy as np 

a = np.linspace(0,2 * np.pi, 100)
fig, axs = plt.subplots(2,2)

axs[0,0].plot(3 * np.cos(a), 3 * np.sin(a))
axs[0,0].set_title('Not equal, parece uma elipse', fontsize = 10)

axs[0,1].plot(3 * np.cos(a), 3 * np.sin(a))
axs[0,1].axis('equal')
axs[0,1].set_title('Círculo', fontsize = 10)

axs[1,0].plot(3 * np.cos(a), 3 * np.sin(a))
axs[1,0].axis('equal')
axs[1,0].set(xlim = (-3,3), ylim=(3,-3))
axs[1,0].set_title('Círculo, mas mudei os limites de visualização', fontsize = 10)

axs[1,1].plot(3 * np.cos(a), 3 * np.sin(a))
axs[1,1].axis('equal')
axs[1,1].set(xlim = (-3,3), ylim=(3,-3))
axs[1,1].set_title('Círculo, mas mudei os limites de visualização', fontsize = 10)

#Continuar com o slide pois eu me perdi no código 


import matplotlib.pyplot as plt
import numpy as np 

N = 5
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind,menMeans,width, yerr = menStd)
p2 = plt.bar(ind,womenMeans,width, bottom = menMeans, yerr = womenStd)
plt.ylabel('Scores')
plt.title('Scores por grupo de idade')
plt.xticks(ind,('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]), ('Men','Women'))

plt.show()

import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0,0.1,0,0)

fig,ax = plt.subplots()
ax.pie(sizes, explode=explode, labels =labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis=('equal')
plt.show()


import matplotlib.pyplot as plt
import numpy as np 
np.random.seed(1968081)
all_data = [np.random.normal(0,std,size=100) for std in range(1,4)]
print(all_data)

labels = ['x1', 'x2', 'x3']
fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(9,4))

bplot = ax.boxplot(all_data, vert=True, patch_artist = True, labels = labels)
ax.set_title('Box plot retangular')

colors = ['pink', 'lightblue', 'lightgreen'] 
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.yaxis.grid(True)
ax.set_xlabel('Teste 1')
ax.set_ylabel('Teste 2')
plt.show()

import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

np.random.seed(1968081)
N_points = 100000
n_bins = 200

x = np.random.randn(N_points)
fig,ax = plt.subplots(1,1, sharey=True, tight_layout=True)

ax.hist(x,bins = n_bins)
ax.set_xlabel('Teste 1')
ax.set_ylabel('Teste 2')
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()
ax = fig.gca(projection='3d')

colors=('r', 'g','b', 'k')
np.random.seed(1968081)

x = np.random.sample(20*len(colors))
y = np.random.sample(20*len(colors))
z = np.random.sample(20*len(colors))

c_list =[]
for c in colors:
    c_list.extend([c]*20)

ax.scatter(x,y,z,c=c_list, label='points')
ax.view_init(elev=20, azim=-35)
plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import cm 
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np 

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)

X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X,Y,Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

fig, ax = plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def init():
    line.set_ydata([np.nan]*len(x))
    return  line,
def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, interval=2, 
                             blit= True, save_count=50)
plt.show()