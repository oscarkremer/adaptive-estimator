import os
import numpy as np 
import matplotlib.pyplot as plt 
from src.models import Estimator

def f(t):
    return np.random.uniform(low=0, high=4, size=t.shape[0])

if __name__=='__main__':
    u, y ,models, thetas, p = [], [], [], [], []
    step = 0.001
    final_time = 0.500
    t = np.arange(0, step + final_time, step)
    update_times = [0.51]
    a = 0.4
    b1 = 2
    b2 = 1.5
    
#   a = 0.4
  #   update_times = [0.03, 0.05, 0.07]
    #update_times = [0.01, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3]
    #u = np.array([np.sin(t), np.cos(t), 3*np.power(t, 2)])
    #print(u.shape)    
#    weights = np.array([3*np.ones(t.shape[0]) + 40*np.sin(10*t), 2*np.ones(t.shape[0]) + 1.1*np.sin(2*t), 6*np.ones(t.shape[0])])
#    y = np.sum(weights*u,axis=0)
#    print(y.shape)
    sig = f(t)

    for i in range(t.shape[0]):
        if i == 0:
            y.append(b2*np.sin(sig[i]))
            u.append([0, 0, 0])
        else:
            y.append(-a*y[i-1] + b1*sig[i-1] + b2*np.sin(sig[i]))        
            u.append([-y[i-1], sig[i-1], np.sin(sig[i])])
    u = np.transpose(np.array(u))
    print(u.shape)
#    print(size(y))
#    for i in range(t.shape[0]):
#        if np.round(t[i],3) < 0.25:
#            y.append([weights[0][0]*u[0][i] + weights[0][1]*u[1][i] + weights[0][2]*u[2][i]])
#        else:
#            if np.round(t[i],3) < 0.26:
#                y.append([weights[1][0]*u[0][i] + weights[1][1]*u[1][i] + weights[1][2]*u[2][i]])
#            else:
#                y.append([weights[2][0]*u[0][i] + weights[2][1]*u[1][i] + weights[2][2]*u[2][i]])  
    analysis = 'error'
#    analysis = 'mean'
    y = np.array(y)
    for update_time in update_times:
        model = Estimator(update_time, step + final_time)
        model.train(t, u, y)
        models.append(model)

    for i in range(t.shape[0]):
        error_list  = []
        if analysis=='error':
            for model in models:
                error_list.append(model.error[i])
            index = np.argmin(np.array(error_list))
        else:
            for model in models:
                error_list.append(model.mean[i])
            index = np.argmin(np.array(error_list))
   #     print(models[index])

        thetas.append(models[index].theta_plot[i])
        
        p.append(models[index].p[i])

    y_hat  = np.zeros(t.shape[0])
    error = np.zeros(t.shape[0])
    for i in range(t.shape[0]):
        y_hat[i] = thetas[i][0]*u[0][i] + thetas[i][1]*u[1][i] + thetas[i][2]*u[2][i]
        error[i] = (y[i] - y_hat[i])/y[i]

    plt.plot(t, y)
    for model in models:
        plt.plot(t, model.y_hat)
    plt.show()

    plt.plot(t,p)
    plt.show()

    for model in models:
        plt.plot(t, np.transpose(np.array(model.theta_plot))[0])
        plt.plot(t, np.transpose(np.array(model.theta_plot))[1])
        plt.plot(t, np.transpose(np.array(model.theta_plot))[2])
        plt.show()

    plt.plot(t, error)
    plt.show()