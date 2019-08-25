import os
import numpy as np 
import matplotlib.pyplot as plt 
from src.models import Estimator

if __name__=='__main__':
    y = []
    t = np.arange(0, 0.5001, 0.001)
    u = [np.sin(t),np.cos(t), 3*np.power(t, 2)]
    for i in range(t.shape[0]):
        if t[i] < 0.3:
            y.append([3*u[0][i] + 2*u[1][i] + 6*u[2][i]])
        else:
            y.append([2*u[0][i] + 2*u[1][i] + 2*u[2][i]])
           
    y = np.array(y)
    model = Estimator(0.1, 0.5)
    theta_plot, p = model.train(t, u, y)
    plt.plot(t,p)
    plt.show()

    theta1 = np.transpose(np.array(theta_plot))[0]
    theta2 = np.transpose(np.array(theta_plot))[1]
    theta3 = np.transpose(np.array(theta_plot))[2]
    
    plt.plot(t, theta1)
    plt.plot(t, theta2)
    plt.plot(t, theta3)
    plt.show()