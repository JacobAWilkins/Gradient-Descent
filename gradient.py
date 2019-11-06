#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jacob Wilkins
"""
    k is the iteration count
    fVal is the sum of squared distances from the current hospital to the cities
    grad is the value of the gradient for the current hospital
    h is the corrdinates of the hospital
"""
from numpy import linalg as LA, sum, array, vstack
import matplotlib.pyplot as plt

def positionHospital(c, h, alpha, tol):
    k = 0; prev = h # initialize k and x_0
    while True:
        # calculate sum of squared differences for x_k
        fv = sum((c[:, 0] - prev[0])**2 + (c[:, 1] - prev[1])**2)
        # calculate gradient of the sum of squared differences for x_k
        g = array([2 * sum(c[:, 0] - prev[0]), 2 * sum(c[:, 1] - prev[1])])
        # calculate x_k+1 and add it to hospitals array
        curr = prev + alpha * g; h = vstack((h, curr))
        print(f"k = {k}, fVal = {fv:.2f}, grad = [{g[0]:.2f}, {g[1]:.2f}]  h = [{curr[0]:.2f}, {curr[1]:.2f}]")
        # return if difference of x_k+1 and x_k is less than tolerance
        if (LA.norm(curr - prev, 2) < tol): return h;
        k += 1; prev = curr # store x_k+1 to use as x_k in next iteration

def plotCoor(cities, hospital):
    for h in hospital: plt.plot(h[0], h[1], 'rx') # plot hospitals
    for c in cities: plt.plot(c[0], c[1], 'bo', mfc='none') # plot cities
    plt.title("Cities and Hospital Locations"); plt.show()

if __name__ == "__main__":
    cities = array([[ 0,   0], [30, 110], [60, 100], [50,  50]]) # coordinates of cities
    hosp = array([0, 55]) # initial coordinates of hospital
    alpha = 0.01 # learning rate
    tol = 1 # used for deciding how long to iterate
    
    hNew = positionHospital(cities, hosp, alpha, tol)
    plotCoor(cities, hNew)
