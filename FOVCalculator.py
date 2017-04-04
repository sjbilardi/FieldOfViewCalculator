
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:49:01 2016

A field of view (FOV) calculator for estimating 
an object's resolution and size in an image
based off the optical system, size of the target
object and distance between observation site 
and object.

@author: sjbilardi
"""

import numpy as np

#%% Telescope System Classes
class Camera():
	def __init__(self, name, pixSize, sensorSize):
		self.name = name
		self.pixSize = pixSize				# microns
		self.sensorSize = sensorSize		# [x, y] pixels

class Telescope():
	def __init__(self, name, diameter, fratio, barlowMagnification=1):
		self.name = name
		self.diameter = diameter*2.54*10								# inch to mm
		self.fratio = fratio				
		self.flength = self.fratio*self.diameter*barlowMagnification	# mm

class Telesystem():
	def __init__(self, Camera, Telescope):
		self.Camera = Camera
		self.Telescope = Telescope
		self.name = [Camera.name, Telescope.name]
		self.resolution = np.arctan(self.Camera.pixSize*10**(-3)/self.Telescope.flength)*3600*180/np.pi 	# arcseconds 
		self.fov = [self.resolution*self.Camera.sensorSize[0], 
									self.resolution*self.Camera.sensorSize[1]] # arcseconds

class ObservationInfo():
	def __init__(self, obj, Telesystem, objDistance=False, objPixSize=False, wavelength=550):
		self.objName = obj[0]
		self.objDistance = objDistance		# km
		self.objSize = [obj[1], obj[2]]		# [height, width] m
		self.wavelength = 550				# nm
		self.Telesystem = Telesystem
		self.diffractionLimit = 1.22*180*3600*self.wavelength*10**(-9)/(self.Telesystem.Telescope.diameter*np.pi/1000)	# arcseconds
		self.resolution = self.Telesystem.resolution*np.pi/(180*3600)
		self.objResolution = np.tan(self.resolution)*(self.objDistance*1000)							# m
		self.objSizePix = [self.objSize[0]/self.objResolution, self.objSize[1]/self.objResolution]		# pixels

#%% Functions
def printResults(obsInfo):
	print('Imaging '+obsInfo.objName+' using '+obsInfo.Telesystem.name[0]+' on '+obsInfo.Telesystem.name[1]+'.')
	print('Imaging from distance %.2fkm.' % obsInfo.objDistance)
	print(obsInfo.objName+' has height %.1fm and width %.1fm.' % (obsInfo.objSize[0], obsInfo.objSize[1]))
	print('Focal length is %.2fmm.' % obsInfo.Telesystem.Telescope.flength)
	print('Angular resolution is %.2f arcseconds/pixel.' % obsInfo.Telesystem.resolution)
	print('Object resolution is %.2f m/pixel.' % obsInfo.objResolution)
	print('Diffraction limit is %.2f acrseconds.' % obsInfo.diffractionLimit)
	print('Object has height %d pixels and width %d pixels.' % (obsInfo.objSizePix[0], obsInfo.objSizePix[1]))

def requiredDistance(obsInfo): 
	requiredRes = obsInfo.objSize[0]/obsInfo.Telesystem.Camera.sensorSize[0]					# m
	requiredDist = requiredRes/(np.tan(obsInfo.Telesystem.resolution*np.pi/(180*3600))*1000)	# km
	print('Required distance for '+obsInfo.objName+' to fill image is %.1fkm.' % requiredDist)
