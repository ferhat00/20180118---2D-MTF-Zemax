# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:06:06 2018

@author: fculfaz
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

detector_MTF1 = 0.64
detector_MTF2 = 0.5

fname = 'content.csv' #Import 2d text file from Zemax into Excel and save as csv

z = np.loadtxt(open("content.csv", "rb"), delimiter=",", skiprows=0)
x = np.linspace(-10,10,num=61) #check that num is same number as set in Zemax for the 2D universal plot
y = np.linspace(-10 ,10,num=61) #Also check begin and end spatial values are the same as in Zemax

#Plot of pure optical MTF of test setup with your optical system, excluding detector MTF
plot1 = plt.figure(1)
z_min, z_max = np.abs(z).min(), np.abs(z).max()
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z, cmap='rainbow', vmin=z_min, vmax=z_max)
plt.colorbar()
plt.title('2D MTF plot Optical')

#Plot of combined optical and detector MTF
plot2 = plt.figure(2)
z_aft1 = np.multiply(z,detector_MTF1)
z_min2, z_max2 = np.abs(z_aft1).min(), np.abs(z_aft1).max()
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z_aft1, cmap='rainbow', vmin=z_min, vmax=z_max)
plt.colorbar()
plt.title('2D MTF plot Overall  - Detector MTF = %f' % detector_MTF1)

plot3 = plt.figure(3)
z_aft2 = np.multiply(z,detector_MTF2)
z_min3, z_max3 = np.abs(z_aft2).min(), np.abs(z_aft2).max()
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z_aft2, cmap='rainbow', vmin=z_min, vmax=z_max)
plt.colorbar()
plt.title('2D MTF plot Overall  - Detector MTF = %f' % detector_MTF2)

plot4 = plt.figure(4)
z_subtr = np.subtract(z,z_max)
z_min4, z_max4 = np.amin(z_subtr), np.amax(z_subtr)
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z_subtr, cmap='rainbow', vmin=z_min4, vmax=z_max4)
plt.colorbar()
plt.title('2D MTF plot Optical  - Subtraction')

plot5 = plt.figure(5)
z_subtr2 = np.subtract(z_aft1,z_max2)
z_min5, z_max5 = np.amin(z_subtr2), np.amax(z_subtr2)
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z_subtr2, cmap='rainbow', vmin=z_min4, vmax=z_max4)
plt.colorbar()
plt.title('2D MTF plot Overall  - Detector MTF = %f - Subtraction' % detector_MTF1)

plot6 = plt.figure(6)
z_subtr3 = np.subtract(z_aft2,z_max3)
z_min6, z_max6 = np.amin(z_subtr3), np.amax(z_subtr3)
plt.xlabel('Y(mm)')
plt.ylabel('X(mm)')
plt.pcolor(x,y,z_subtr3, cmap='rainbow', vmin=z_min4, vmax=z_max4)
plt.colorbar()
plt.title('2D MTF plot Overall  - Detector MTF = %f - Subtraction' % detector_MTF2)

pp = PdfPages('plots.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.savefig(plot4)
pp.savefig(plot5)
pp.savefig(plot6)
pp.close()