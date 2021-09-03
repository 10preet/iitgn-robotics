import math
import numpy as np
import scipy

d=int(input())
l1=int(input())
l2=int(input())
l3=int(input())
Theta_1=int(input("Enter in degree "))
Theta_2=int(input("Enter in degree"))
q1=Theta_1*(np.pi/180)
q2=Theta_2*(np.pi/180)

p3=np.vstack([0,0,d])

R1_2 = np.array([[np.cos(q2), -np.sin(q2),0],[np.sin(q2),np.cos(q2),0],[0,0,1]])
R0_1 = np.array([[np.cos(q1), -np.sin(q1),0],[np.sin(q1),np.cos(q1),0],[0,0,1]])

d2_3=np.vstack([l3,0,0])
d1_2=np.vstack([l2,0,0])
d0_1=np.vstack([0,0,l1])

R2_3 = np.array([[1,0,0],[0,1,0],[0,0,1]])

# [[p0] = H0_1 * H1_2 * H2_3 * [[p3]
#  [1]]                         [1]]

p0 = np.vstack([l2*np.cos(q1) + l3*np.cos(q1+q2),l2*np.sin(q1) + l3*np.sin(q1+q2),l1 + d])

print(p0, "The position vector of End-effector")

