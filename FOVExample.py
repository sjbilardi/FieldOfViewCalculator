import FOVCalculator as fov

# Distances
avg_plane_alt = 35000 * 0.3048/1000			# kilometers (average)

# Objects
boing737 = ['Boing 737-100', 28.65, 28.35] 	# meters [name, height, width] (Boing)

# Manta, C14 Optical System (Boing 737)
manta = fov.Camera(name='Allied Vision Manta G-235', pixSize=5.86, sensorSize=[1936, 1216])
C14 = fov.Telescope(name='Celestron C14 Edge HD', diameter=14, fratio=11, barlowMagnification=1) 
mantaC14 = fov.Telesystem(Camera=manta, Telescope=C14)
MC_obsInfo = fov.ObservationInfo(obj=boing737, objDistance=avg_plane_alt, Telesystem=mantaC14)
fov.printResults(obsInfo=MC_obsInfo)
fov.requiredDistance(obsInfo=MC_obsInfo)
