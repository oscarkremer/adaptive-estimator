import os
import numpy as np 
import matplotlib.pyplot as plt 


if __name__=='__main__':
    t = np.arange(0, 0.5001, 0.001)
    u = [np.sin(t),np.cos(t), 3*np.power(t, 2)]
    y, theta_plot = [], []

    for i in range(t.shape[0]):
        if t[i] < 0.3:
            y.append([3*u[0][i] + 2*u[1][i] + 6*u[2][i]])
        else:
            y.append([2*u[0][i] + 2*u[1][i] + 2*u[2][i]])
           
    y = np.array(y)
    P = 100000*np.identity(3)
    p = np.zeros(t.shape[0])
    theta = [0, 0, 0]
    for i in range(t.shape[0]):
        theta_plot.append(theta)
        p[i] = np.linalg.norm(P, ord='fro')
        fi = np.array([[u[0][i]], [u[1][i]], [u[2][i]]])
        K = P.dot(fi)/(1 + (np.transpose(fi).dot(P)).dot(fi))
        P = (np.identity(3) - K.dot(np.transpose(fi))).dot(P)
        if t[i] in [0.1, 0.2, 0.3, 0.4]:
            P = 100000*np.identity(3)
        theta = theta + K.dot(y[i] - np.transpose(fi).dot(theta))

    plt.plot(t,p)
    plt.show()

    theta1 = np.transpose(np.array(theta_plot))[0]
    theta2 = np.transpose(np.array(theta_plot))[1]
    theta3 = np.transpose(np.array(theta_plot))[2]
    
    plt.plot(t, theta1)
    plt.plot(t, theta2)
    plt.plot(t, theta3)
    plt.show()