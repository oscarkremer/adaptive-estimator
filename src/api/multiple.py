import os
import numpy as np 
import matplotlib.pyplot as plt 
from src.models import Estimator

if __name__=='__main__':
    y ,models, thetas, p = [], [], [], []
    step = 0.001
    final_time = 0.500
    t = np.arange(0, step + final_time, step)
    update_times = [0.01, 0.03, 0.05, 0.07]
    #update_times = [0.01, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3]
    u = [np.sin(t), np.cos(t), 3*np.power(t, 2)]
    weights = [[3, 2, 6],[10, 12, 6],[20, 0, 30]]
    print(weights[0][0])
    print(weights[1][0])
    print(weights[2][0])
    
    for i in range(t.shape[0]):
        if np.round(t[i],3) < 0.25:
            y.append([weights[0][0]*u[0][i] + weights[0][1]*u[1][i] + weights[0][2]*u[2][i]])
        else:
            if np.round(t[i],3) < 0.42:
                y.append([weights[1][0]*u[0][i] + weights[1][1]*u[1][i] + weights[1][2]*u[2][i]])
            else:
                y.append([weights[2][0]*u[0][i] + weights[2][1]*u[1][i] + weights[2][2]*u[2][i]])  
    analysis = 'error'
#    analysis = 'mean'
    y = np.array(y)
    for update_time in update_times:
        model = Estimator(update_time, step + final_time)
        print(model)
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
                print(model.mean[i])
            index = np.argmin(np.array(error_list))
        print(index)
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

    plt.plot(t, y)
    plt.plot(t, y_hat)
    plt.show()


#    plt.plot(t, np.transpose(np.array(thetas))[0])
#    plt.plot(t, np.transpose(np.array(thetas))[1])
#    plt.plot(t, np.transpose(np.array(thetas))[2])
#    plt.show()

    plt.plot(t, error)
    plt.show()