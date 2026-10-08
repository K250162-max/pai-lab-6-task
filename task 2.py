import numpy as np

# 10 rows = 10 samples
# 4 columns = 4 features
features = np.array([
    [10, 20, 30, 40],
    [12, 22, 32, 42],
    [14, 24, 34, 44],
    [16, 26, 36, 46],
    [18, 28, 38, 48],
    [20, 30, 40, 50],
    [22, 32, 42, 52],
    [24, 34, 44, 54],
    [26, 36, 46, 56],
    [28, 38, 48, 58]
])

# Mean of each feature
mean = np.mean(features, axis=0)

# Standard deviation of each feature
std = np.std(features, axis=0)

# Standardize each feature
standardized = (features - mean) / std

print("Original features:")
print(features)

print("\nMean of each feature:")
print(mean)

print("\nStandard deviation of each feature:")
print(std)

print("\nStandardized features:")
print(standardized)

# Verify mean and standard deviation
print("\nNew means:")
print(np.mean(standardized, axis=0))

print("\nNew standard deviations:")
print(np.std(standardized, axis=0))