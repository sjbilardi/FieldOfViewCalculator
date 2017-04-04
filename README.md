# FieldOfViewCalculator
Calculates the field of view for a given camera and telescope and expected ideal resolution.

## Use

**Required packages:** Numpy

Run the "FOVExample.py" file. Note the units for all class and function parameters (also in comments).

- "pixSize:" microns
- "sensorSize:" number of pixels
- "diameter:" inches
- "wavelgenth:" nanometers
- "objDistance:" kilometers
- object size is assumed to be in meters

1. Define a camera using "Camera" class with parameters:
  - camera name
  - pixel size 
  - sensor size
2. Define a telescope using "Telescope" class with parameters:
  - Name
  - Diameter
  - f ratio
  - Barlow magnification factor (defaulted to 1)
3. Define optical system using "Telesystem" class using:
  - Defined camera class
  - Defined telescope class
4. Get observation info using "ObservationInfo" class using:
  - Object of interest (array of name, height, width)
  - Defined "Telesystem" class
  - Object distance or Object size in pixels in image
5. Use function "printResults()" to print results.
6. Use function "requiredDistance()" to print required distance needed to be to fit object in image.
