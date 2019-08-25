import os
import numpy as np 
import matplotlib.pyplot as plt 



if __name__=='__main__':
    t = np.linspace(0,0.5,501)
    u1 = np.sin(t)
    u2 = np.cos(t)
    u3 = 3*np.power(t, 2)
    y = np.transpose(np.array([3*u1+ 2*u2+ 6*u3]))
    print(y.shape)
    P = 10000*np.identity(3)
#    theta_plot = zeros(3, 501)
    p = np.zeros(501)
    theta = [0, 0, 0]
    for i in range(501):
        p[i] = np.linalg.norm(P, ord='fro')
        fi = np.array([[u1[i]], [u2[i]], [u3[i]]])
        K = P.dot(fi)/(1 + (np.transpose(fi).dot(P)).dot(fi))
        P = (np.identity(3) - K.dot(np.transpose(fi))).dot(P)
        print(P)
        theta = theta + K.dot(y[i] - np.transpose(fi).dot(theta))
        print(theta)
    plt.plot(t,p)
    plt.show()