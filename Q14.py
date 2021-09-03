import math
import numpy as np
import scipy

l1=int(input())
l2=int(input())
l3=int(input())
Theta_1=int(input("Enter in degree"))
Theta_2=int(input("Enter in degree"))
Theta_3=int(input("Enter in degree"))
q1=Theta_1*np.pi/180
q2=Theta_2*np.pi/180
q3=Theta_3*np.pi/180


J=np.array([[-(l1*np.sin(q1)+l2*np.sin(q1+q2)+l3*np.sin(q1+q2+q3)),-(l2*np.sin(q1+q2)+l3*np.sin(q1+q2+q3)),-l3*np.sin(q1+q2+q3)],[l1*np.cos(q1)+l2*np.cos(q1+q2)+l3*np.cos(q1+q2+q3),l2*np.cos(q1+q2)+l3*np.cos(q1+q2+q3),l3*np.cos(q1+q2+q3)],[0,0,0],[0,0,0],[0,0,0],[1,1,1]])
print("The Jacobian manipulator for RRR is", J)