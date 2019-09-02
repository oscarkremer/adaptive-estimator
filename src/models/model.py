import os
import numpy as np 
import matplotlib.pyplot as plt 

class Estimator:
    def __init__(self, delta_time, final_time, rastreabilty = 1000000):
        self.rastreabilty = rastreabilty
        self.update_time = delta_time
        self.final_time = final_time

    def create_timelist(self):
        time_list = []
        append_time = self.update_time
        while append_time < self.final_time:
            time_list.append(np.round(append_time,2))
            append_time+=self.update_time
        return time_list

    def train(self, t, u, y, lambda_forg=1):
        error, theta_plot = [], []
        self.P = self.rastreabilty*np.identity(3)
        p = np.zeros(t.shape[0])
        y_hat = np.zeros(t.shape[0])
        norm = np.zeros(t.shape[0])
        mean = np.zeros(t.shape[0])
        theta = [0, 0, 0]
        time_list = self.create_timelist()
        for i in range(t.shape[0]):
            if np.round(t[i], 3) in time_list:
                self.P = self.rastreabilty*np.identity(3)
            error.append(abs(y[i] - theta[0]*u[0][i] - theta[1]*u[1][i] - theta[2]*u[2][i])/y[i])
            p[i] = np.linalg.norm(self.P, ord='fro')
            norm[i] = p[i]/np.linalg.norm(self.rastreabilty*np.identity(3), ord='fro')
            theta_plot.append(theta)
            fi = np.array([[u[0][i]], [u[1][i]], [u[2][i]]])
            K = self.P.dot(fi)/(lambda_forg + (np.transpose(fi).dot(self.P)).dot(fi))
            self.P = (np.identity(3) - K.dot(np.transpose(fi))).dot(self.P)/lambda_forg
            theta = theta + K.dot(y[i] - np.transpose(fi).dot(theta))
            y_hat[i] = theta_plot[i][0]*u[0][i] + theta_plot[i][1]*u[1][i] + theta_plot[i][2]*u[2][i]
        self.y_hat = y_hat
        self.error = error
        self.theta_plot= theta_plot
        self.p = p
        self.mean = mean


