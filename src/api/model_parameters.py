import os
import numpy as np 
import matplotlib.pyplot as plt 



if __name__=='__main__':
    t = np.linspace(0,0.5,501)
    u1 = np.sin(t)
    u2 = np.cos(t)
    u3 = 3*np.power(t, 2)
    y = []
    for i in range(501):
        if t[i] < 0.2:
            y.append([3*u1[i] + 2*u2[i] + 6*u3[i]])
        else:
            if t[i] < 0.4:
                y.append([2*u1[i] + 2*u2[i] + 2*u3[i]])
            else:
                y.append([u1[i] + u2[i] + u3[i]])
           
    y = np.array(y)
    print(y.shape)
    P = 10000*np.identity(3)
#    theta_plot = zeros(3, 501)
    p = np.zeros(501)
    theta = [0, 0, 0]
    theta_plot = []
    for i in range(501):
        theta_plot.append(theta)
        p[i] = np.linalg.norm(P, ord='fro')
        fi = np.array([[u1[i]], [u2[i]], [u3[i]]])
        K = P.dot(fi)/(1 + (np.transpose(fi).dot(P)).dot(fi))
        P = (np.identity(3) - K.dot(np.transpose(fi))).dot(P)
        print(P)
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