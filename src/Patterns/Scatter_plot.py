'''
Created on Sep 12, 2016

@author: abhin
'''
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib


'''
N = 50
x = np.random.rand(2)
y = np.random.rand(2)
print(x)
print(y)
y_attr = np.array(["", ""])
x_attr = np.array(["first_serveWon", "fault"])
radii = [5.2, -4.6]
radii = np.asarray(radii) 
#print(type(x))
#print(x.shape)
#colors = np.random.rand(2)
colors = np.array(['r', 'b'])
#print(colors)
#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
area = np.pi * (10 * radii)**2 
print(area)

plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap=matplotlib.colors.ListedColormap(colors))
plt.yticks(y, y_attr, size= 'small')
plt.xticks(x, x_attr, size='small')
plt.title("jaffa")
plt.ylabel("total point won")
plt.grid()
loc = [0, 1]
#cb = plt.colorbar()
#cb.set_ticks(loc)
#cb.set_ticklabels(["negative", "positive"])
plt.show()
'''
from numpy import *
from matplotlib.pyplot import *
from numpy.random import *

a = rand(4,4)

[b,c,d,e] = plot(a)
legend([b,c,d,e], ["b","c","d","e"], loc=1)
show()

'''
x = [4,8,12,16,1,4,9,16]
y = [1,4,9,16,4,8,12,3]
label = [0,1,2,3,0,1,2,3]
colors = ['red','green','blue','purple']

fig = plt.figure(figsize=(8,8))
plt.scatter(x, y, c=label, cmap=matplotlib.colors.ListedColormap(colors))

cb = plt.colorbar()
loc = np.arange(0,max(label),max(label)/float(len(colors)))
print(loc)
cb.set_ticks(loc)
cb.set_ticklabels(colors)
plt.show()

'''