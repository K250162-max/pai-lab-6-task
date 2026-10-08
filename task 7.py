import numpy as np

# Create an array with some NaN values
data = np.array([10, 20, np.nan, 30, np.nan, 40, 50])

# Detect NaN values
nan_values = np.isnan(data)

# NaN-aware statistics
mean = np.nanmean(data)
minimum = np.nanmin(data)
maximum = np.nanmax(data)
std = np.nanstd(data)

# Replace NaN values with the mean
data[np.isnan(data)] = mean

# Verify that no NaN values remain
remaining_nan = np.isnan(data)

print("Original array:")
print(data)

print("\nNaN values:")
print(nan_values)

print("\nMean:", mean)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard deviation:", std)

print("\nArray after replacing NaN:")
print(data)

print("\nNaN remaining:")
print(np.any(remaining_nan))