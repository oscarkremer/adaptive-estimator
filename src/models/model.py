import os
import numpy as np 
import matplotlib.pyplot as plt 

class Estimator:
    def __init__(self, delta_time, final_time):
        self.update_time = delta_time
        self.final_time = final_time

    def create_timelist(self):
        time_list = []
        append_time = self.update_time
        while append_time < self.final_time:
            time_list.append(np.round(append_time,2))
            append_time+=self.update_time
        return time_list

    def train(self, t, u, y):
        error, theta_plot = [], []
        P = 100000*np.identity(3)
        p = np.zeros(t.shape[0])
        theta = [0, 0, 0]
        time_list = self.create_timelist()
        for i in range(t.shape[0]):
            theta_plot.append(theta)
            p[i] = np.linalg.norm(P, ord='fro')
            fi = np.array([[u[0][i]], [u[1][i]], [u[2][i]]])
            K = P.dot(fi)/(1 + (np.transpose(fi).dot(P)).dot(fi))
            P = (np.identity(3) - K.dot(np.transpose(fi))).dot(P)
            if np.round(t[i],3) in time_list:
                P = 100000*np.identity(3)
            theta = theta + K.dot(y[i] - np.transpose(fi).dot(theta))
            error.append(abs(y[i] - theta[0]*u[0][i] + theta[1]*u[1][i] + theta[2]*u[2][i]))
        self.error = error
        return theta_plot, p
           

