#!/usr/bin/env python
"""
Initial code for Electric Field of a Charge Distribution (Newman 5.21)
======================================================================

This is a base implementation of exercise 5.21 that plots the electric potential and 
electric field of two point charges with opposite signs. 

For a charge distribution, the potential may be found as the summation of the potential due
to each individual charge, while the electric field is simply the negative gradient of the
potential function.

Parts of the code with '...' will need to be completed.
Comments prepended with ### are guide questions.
"""

__author__ = "Micholo Medrana"
__credits__ = "Mark Newman"

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

# Initialize potential due to charges
q1 = 1
q2 = -1
q1loc = (0,-10) #location of charge 1
q2loc = (0,10) #location of charge 2

potential_arr = np.array(np.zeros((101,101))) # initialize potential array

def potential(curcoord): 
    '''
    Function to calculate electric potential due to our two charges at a location curcoord = (y, x)
    '''
    rq1 = np.sqrt((q1loc[0]-curcoord[0])**2 + (q1loc[1]-curcoord[1])**2) # calculate distance of location to charge 1
    rq2 = ... # calculate distance of location to charge 2
    if (rq1 != 0) and (rq2 != 0): # if our current coordinate is not at the charge
        return ... # calculate potential
    else:
        return 0 # potential diverges at locations of charges

for y, row in enumerate(potential_arr):
    for x, val in enumerate(row):
        curcoord = (y-50, x-50) # get current coordinates
        ### Why must we subtract 50 from x and y here? hint: Python indexing
        potential_arr[y,x] = potential(curcoord)

# Visualize our potential

xgrid = np.linspace(-50,50,101)
ygrid = np.linspace(-50,50,101)

# fig = plt.figure()
# ax = fig.add_subplot(111)

fig, (ax1, ax2) = plt.subplots(figsize=(8, 3), ncols=2)
#pot = ax1.imshow(potential_arr)
pot = ax1.contourf(xgrid, ygrid, potential_arr, cmap='RdBu_r')
ax1.contour(xgrid, ygrid, potential_arr, colors='k', linestyles='solid')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_xlim(-15,15)
ax1.set_ylim(-15,15)
ax1.set_aspect('equal')
fig.colorbar(pot,ax=ax1)
### Add a title to this subfigure.

# Calculate E = -gradient phi
# note that gradient (2D) is just (\partial f/\partial x) xhat + (\partial f/\partial y) yhat

h = 0.01 # Choose some h.
### Can we adaptively optimize this value to be within a reasonable error?

Ex = np.array(np.zeros((101,101))) #initialize array for x-components of field
Ey = np.array(np.zeros((101,101))) #initialize array for y-components of field
for y, row in enumerate(Ex):
    for x, val in enumerate(row):
        ### Complete the following statements to get partial-x and partial-y (central difference approximation).
        ### Remember that you need to subtract 50 from y and x before inputting them into the potential function.
        ### Also remember the order with which the potential function accepts values!
        partialx = ...
        Ex[y,x] = ...
        partialy = ...
        Ey[y,x] = ...

# Plot the electric field using streamplot
color = 2 * np.log(np.hypot(Ex,Ey))
ele = ax2.streamplot(xgrid, ygrid, Ex, Ey, color=color, linewidth=1, cmap = plt.cm.inferno,
             density=2, arrowstyle='->', arrowsize=1.5)
             ### Study the parameters of the streamplot function. What does each do?
             ### See: https://matplotlib.org/gallery/images_contours_and_fields/plot_streamplot.html
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_xlim(-50,50)
ax2.set_ylim(-50,50)
ax2.set_aspect('equal')
fig.colorbar(ele.lines,ax=ax2)
### Add a title to this subfigure.
plt.show()

### Check your plots and see if they correspond to that of a dipole potential and electric field.
### For enrichment, you can modify the code to plot the field of a quadrupole, octapole, or any 
### arbitrary charge distribution.