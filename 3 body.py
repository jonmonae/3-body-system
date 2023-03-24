
# importing numpy
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
ax = plt.axes(projection='3d')
ax.grid()
  
t = 0.003


# Initial conditions 
pos1 = [4.49, 0, 0]
pos2 = [-4.49, 0, 0]
pos3 = [0.01, 0, 5]

vel1 = [0,0.385,0.001]
vel2 = [0,-0.385,0.001]
vel3 = [0,0,0]

m1 = 250
m2 = 250
m3 = 1


#Gravitational constant
G = 75


#converting init conditions from lists to vectors
r1 = np.array(pos1)
print("r1  : " + str(r1))
v1 = np.array(vel1)
print("v1  : " + str(v1))


r2 = np.array(pos2)
print("r2  : " + str(r2))
v2 = np.array(vel2)
print("v2  : " + str(v2))


r3 = np.array(pos3)
print("r2  : " + str(r2))
v3 = np.array(vel3)
print("v2  : " + str(v3))


#creating sets for graphing later
x1s = [pos1[0]]
y1s = [pos1[1]]
z1s = [pos1[2]]

x2s = [pos2[0]]
y2s = [pos2[1]]
z2s = [pos2[2]]

x3s = [pos3[0]]
y3s = [pos3[1]]
z3s = [pos3[2]]

for x in range(0, 4000):	


	#vector dxy from object x to y
	d12  = r2 - r1
	d23  = r3 - r2
	d31  = r1 - r3

	#distance between to objects
	magd12 = d12.dot(d12)
	magd23 = d23.dot(d23)
	magd31 = d31.dot(d31)


	#acceleration vectors
	a1 = ((G*m2*(1/magd12)*(1/magd12)*(1/magd12)) * d12) + ((-1)*(G*m3*(1/magd31)*(1/magd31)*(1/magd31)) * d31)
	a2 = ((G*m3*(1/magd23)*(1/magd23)*(1/magd23)) * d23) + ((-1)*(G*m1*(1/magd12)*(1/magd12)*(1/magd12)) * d12)
	a3 = ((G*m1*(1/magd31)*(1/magd31)*(1/magd31)) * d31) + ((-1)*(G*m2*(1/magd23)*(1/magd23)*(1/magd23)) * d23)


	#adjust velocity vectors by some increment
	v1 = v1 + (a1 * t)
	v2 = v2 + (a2 * t)
	v3 = v3 + (a3 * t)

	#adjust position vectors based on velocities
	r1 = r1 + (v1 * t)
	r2 = r2 + (v2 * t)
	r3 = r3 + (v3 * t)


	#add the new positions to the sets used to graph
	x1s.append(r1[0])
	x2s.append(r2[0])
	x3s.append(r3[0])

	y1s.append(r1[1])
	y2s.append(r2[1])
	y3s.append(r3[1])

	z1s.append(r1[2])
	z2s.append(r2[2])
	z3s.append(r3[2])



#plot the set of positions 
ax.plot3D(x1s, y1s, z1s,'blue')
ax.plot3D(x2s, y2s, z2s, 'green')
ax.plot3D(x3s, y3s, z3s, 'red')



ax.set_title('3 body system')
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])



plt.show()


