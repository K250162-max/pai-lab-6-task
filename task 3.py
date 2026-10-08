import numpy as np

# Grayscale image
image = np.array([
    [20, 50, 80, 120],
    [30, 70, 100, 150],
    [40, 90, 130, 180],
    [60, 110, 160, 200]
])

# Minimum intensity
minimum = np.min(image)

# Maximum intensity
maximum = np.max(image)

# Mean intensity
mean = np.mean(image)

# Threshold
threshold = 100

# Binary mask
mask = image > threshold

# Thresholded image
thresholded = np.where(image > threshold, 255, 0)

print("Image:")
print(image)

print("\nMinimum intensity:")
print(minimum)

print("\nMaximum intensity:")
print(maximum)

print("\nMean intensity:")
print(mean)

print("\nBinary mask:")
print(mask)

print("\nThresholded image:")
print(thresholded)