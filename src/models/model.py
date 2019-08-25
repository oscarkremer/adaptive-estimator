import os
import numpy as np 
import matplotlib.pyplot as plt 

class Estimator:
    def __init__(self, delta_time, final_time):
        self.update_time = delta_time
        self.final_time = final_time
 
    def train(self, t, u, y):
        theta_plot = []
        P = 100000*np.identity(3)
        p = np.zeros(t.shape[0])
        theta = [0, 0, 0]
        time_list = self.create_timelist()
        print(time_list)
        for i in range(t.shape[0]):
            theta_plot.append(theta)
            p[i] = np.linalg.norm(P, ord='fro')
            fi = np.array([[u[0][i]], [u[1][i]], [u[2][i]]])
            K = P.dot(fi)/(1 + (np.transpose(fi).dot(P)).dot(fi))
            P = (np.identity(3) - K.dot(np.transpose(fi))).dot(P)
            if np.round(t[i],3) in time_list:
                P = 100000*np.identity(3)
            theta = theta + K.dot(y[i] - np.transpose(fi).dot(theta))
        return theta_plot, p
           
    def create_timelist(self):
        time_list = []
        append_time = self.update_time
        while append_time < self.final_time:
            time_list.append(np.round(append_time,2))
            append_time+=self.update_time
        return time_list

