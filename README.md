# Gradient-Descent
Minimizes the sum of squared distances from a hospital to the neighboring cities using gradient descent. A graph is displayed showing the locations of the cities and the location of the hospital at each iteration.

### Run
```
python gradient.py
```

### Output
k is the iteration count, fVal is the sum of squared distances from the current hospital to the cities, grad is the value of the gradient for the current hospital, and h is the corrdinates of the hospital.

Output for the given cities corrdinates and initial hospital coordinates:
```
k = 0, fVal = 15100.00, grad = [280.00, 80.00]  h = [2.80, 55.80]
k = 1, fVal = 14285.92, grad = [257.60, 73.60]  h = [5.38, 56.54]
k = 2, fVal = 13596.88, grad = [236.99, 67.71]  h = [7.75, 57.21]
k = 3, fVal = 13013.68, grad = [218.03, 62.30]  h = [9.93, 57.84]
k = 4, fVal = 12520.06, grad = [200.59, 57.31]  h = [11.93, 58.41]
k = 5, fVal = 12102.26, grad = [184.54, 52.73]  h = [13.78, 58.94]
k = 6, fVal = 11748.63, grad = [169.78, 48.51]  h = [15.48, 59.42]
k = 7, fVal = 11449.32, grad = [156.20, 44.63]  h = [17.04, 59.87]
k = 8, fVal = 11195.99, grad = [143.70, 41.06]  h = [18.47, 60.28]
k = 9, fVal = 10981.56, grad = [132.21, 37.77]  h = [19.80, 60.66]
k = 10, fVal = 10800.07, grad = [121.63, 34.75]  h = [21.01, 61.00]
k = 11, fVal = 10646.46, grad = [111.90, 31.97]  h = [22.13, 61.32]
k = 12, fVal = 10516.45, grad = [102.95, 29.41]  h = [23.16, 61.62]
k = 13, fVal = 10406.40, grad = [94.71, 27.06]  h = [24.11, 61.89]
```
