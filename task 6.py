import numpy as np

# ------------------ First experiment ------------------

rng1 = np.random.default_rng(42)

# Generate 1000 values from a normal distribution
data1 = rng1.normal(loc=50, scale=10, size=1000)

mean1 = np.mean(data1)
median1 = np.median(data1)
std1 = np.std(data1)
minimum1 = np.min(data1)
maximum1 = np.max(data1)

# Values within one standard deviation of the mean
inside1 = (data1 >= mean1 - std1) & (data1 <= mean1 + std1)

percentage1 = np.mean(inside1) * 100

print("Experiment 1")
print("Mean:", mean1)
print("Median:", median1)
print("Standard deviation:", std1)
print("Minimum:", minimum1)
print("Maximum:", maximum1)
print("Percentage inside 1 standard deviation:", percentage1)


# ------------------ Second experiment ------------------

rng2 = np.random.default_rng(100)

data2 = rng2.normal(loc=50, scale=10, size=1000)

mean2 = np.mean(data2)
median2 = np.median(data2)
std2 = np.std(data2)
minimum2 = np.min(data2)
maximum2 = np.max(data2)

inside2 = (data2 >= mean2 - std2) & (data2 <= mean2 + std2)

percentage2 = np.mean(inside2) * 100

print("\nExperiment 2")
print("Mean:", mean2)
print("Median:", median2)
print("Standard deviation:", std2)
print("Minimum:", minimum2)
print("Maximum:", maximum2)
print("Percentage inside 1 standard deviation:", percentage2)