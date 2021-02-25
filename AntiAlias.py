# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:28:14 2021

@author: msi
"""
import numpy as np
import matplotlib.pyplot as plt


def make_circle2(N):
    radius = N/2 
    matrix2 = np.zeros((N,N,3))

    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            if  (((radius - i)**2) + ((radius - j)**2))**(1/2) < radius:
                matrix2[i][j][2] = 1
            else:
                matrix2[i][j] = 1
    return matrix2  
          
def make_circle():
    
    radius = 200 
    matrix2 = np.zeros((500,500,3))

    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            if  (((radius + 50 - i)**2) + ((radius + 50 - j)**2))**(1/2) < radius:
                matrix2[i][j][2] = 1
            else:
                matrix2[i][j] = 0
    return matrix2

def anti_alias(matrix2, T):
    K = 0
    while K != T:
        K = K + 1
        for i in range(len(matrix2)-1):
            for j in range(len(matrix2[i])-1):
                matrix2[i][j][2] = (matrix2[i][j + 1][2] + matrix2[i][j - 1][2] + matrix2[i + 1 ][j][2] + matrix2[i - 1][j][2])/4
    return matrix2
            
def visualize(matrix):
    plt.figure(dpi=150,facecolor=(1,1,1))
    return plt.imshow(matrix)
visualize(anti_alias(make_circle(),2))