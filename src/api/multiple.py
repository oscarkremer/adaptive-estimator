import os
import numpy as np 
import matplotlib.pyplot as plt 
from src.models import Estimator

if __name__=='__main__':
    y ,models, thetas, p = [], [], [], []
    t = np.arange(0, 0.5001, 0.001)
    update_times = [0.03, 0.07, 0.09, 0.1]

    u = [np.sin(t), np.cos(t), 3*np.power(t, 3)]

    for i in range(t.shape[0]):
        if np.round(t[i],3) < 0.3:
            y.append([3*u[0][i] + 2*u[1][i] + 6*u[2][i]])
        else:
            y.append([2*u[0][i] + 2*u[1][i] + 2*u[2][i]])
           
    y = np.array(y)
    for update_time in update_times:
        model = Estimator(update_time, 0.5)
        model.train(t, u, y)
        models.append(model)

    for i in range(t.shape[0]):
        error_list = []
        for model in models:
            error_list.append(model.error[i])
        index = np.argmin(np.array(error_list))
        
        thetas.append(models[index].theta_plot[i])
        
        p.append(models[index].p[i])

    y_hat  = np.zeros(t.shape[0])

    for i in range(t.shape[0]):
        y_hat[i] = thetas[i][0]*u[0][i] + thetas[i][1]*u[1][i] + thetas[i][2]*u[2][i]

    plt.plot(t, y)
    plt.plot(t, y_hat)
    plt.show()

    plt.plot(t,p)
    plt.show()

    plt.plot(t, np.transpose(np.array(thetas))[0])
    plt.plot(t, np.transpose(np.array(thetas))[1])
    plt.plot(t, np.transpose(np.array(thetas))[2])
    plt.show()
    plt.plot(t, model.error)
    plt.show()