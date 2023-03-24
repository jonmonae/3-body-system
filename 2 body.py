
# importing numpy
import numpy as np
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
ax = plt.axes(projection='3d')
ax.grid()
  
t = 0.003


pos1 = [4.49, 0, 0]
pos2 = [-4.49, 0, 0]

vel1 = [0,0.3798,0.001]
vel2 = [0,-0.3798,0.001]


m1 = 25
m2 = 25


G = 75

r1 = np.array(pos1)
print("r1  : " + str(r1))
v1 = np.array(vel1)
print("v1  : " + str(v1))

  

r2 = np.array(pos2)
print("r2  : " + str(r2))
v2 = np.array(vel2)
print("v2  : " + str(v2))






x1s = [pos1[0]]
y1s = [pos1[1]]
z1s = [pos1[2]]

x2s = [pos2[0]]
y2s = [pos2[1]]
z2s = [pos2[2]]


for x in range(0, 45000):	

	d  = r2 - r1
	magd = d.dot(d)


	a1 = (G*m1*(1/magd)*(1/magd)*(1/magd)) * d
	a2 = (-1*G*m2*(1/magd)*(1/magd)*(1/magd)) * d







	v1 = v1 + (a1 * t)
	v2 = v2 + (a2 * t)

	r1 = r1 + (v1 * t)
	r2 = r2 + (v2 * t)

	x1s.append(r1[0])
	x2s.append(r2[0])

	y1s.append(r1[1])
	y2s.append(r2[1])

	z1s.append(r1[2])
	z2s.append(r2[2])







ax.plot3D(x1s, y1s, z1s,'red')
ax.plot3D(x2s, y2s, z2s, 'blue')


ax.set_title('2 body system')




plt.show()


