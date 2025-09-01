import numpy as np

# Sample dataset (e.g., sales data with missing values)
data = np.array([
    [100, 200, np.nan, 400],
    [150, 250, 300, np.nan],
    [np.nan, 220, 310, 410],
    [180, np.nan, 320, 420]
])

# Handling missing values (replace NaN with column mean)
col_means = np.nanmean(data, axis=0)
indices = np.where(np.isnan(data))
data[indices] = np.take(col_means, indices[1])

print("Cleaned Data:\n", data)

# Basic statistical analysis
mean = np.mean(data, axis=0)
median = np.median(data, axis=0)
std_dev = np.std(data, axis=0)

print("\nColumn Means:", mean)
print("Column Medians:", median)
print("Column Standard Deviations:", std_dev)

# Finding min and max values
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)

print("\nMinimum Values:", min_values)
print("Maximum Values:", max_values)

# Summing across rows and columns
row_sums = np.sum(data, axis=1)
col_sums = np.sum(data, axis=0)

print("\nRow Sums:", row_sums)
print("Column Sums:", col_sums)

# Normalizing data (scaling between 0 and 1)
min_val = np.min(data)
max_val = np.max(data)
normalized_data = (data - min_val) / (max_val - min_val)

print("\nNormalized Data:\n", normalized_data)

