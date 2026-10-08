import numpy as np

# 4 sensors, 5 time points
readings = np.array([
    [20, 22, 25, 23, 21],   # Sensor 1
    [30, 32, 31, 35, 33],   # Sensor 2
    [15, 18, 17, 16, 19],   # Sensor 3
    [40, 42, 45, 43, 44]    # Sensor 4
])

# Mean of each sensor
sensor_mean = np.mean(readings, axis=1)

# Minimum reading of each sensor
sensor_min = np.min(readings, axis=1)

# Maximum reading of each sensor
sensor_max = np.max(readings, axis=1)

# Standard deviation of each sensor
sensor_std = np.std(readings, axis=1)

# Sensor with highest average
highest_sensor = np.argmax(sensor_mean)

# Selected threshold
threshold = 35

# Detect readings above threshold
above_threshold = readings > threshold

print("Sensor readings:")
print(readings)

print("\nMean of each sensor:")
print(sensor_mean)

print("\nMinimum of each sensor:")
print(sensor_min)

print("\nMaximum of each sensor:")
print(sensor_max)

print("\nStandard deviation of each sensor:")
print(sensor_std)

print("\nSensor with highest average:")
print(highest_sensor + 1)

print("\nReadings above threshold:")
print(above_threshold)