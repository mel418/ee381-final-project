import numpy as np
import matplotlib.pyplot as plt

def analyze_population(data, population_name):
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data)

    # Plot histogram
    plt.hist(data, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {population_name}')
    plt.grid(True)
    plt.show()

    print(f"Mean of {population_name}:", mean)
    print(f"Standard Deviation of {population_name}:", std_dev)

    # Define the specific (n, k) pairs
    specific_pairs = [
        (10, 10), (10, 50), (10, 100),
        (50, 10), (50, 50), (50, 100),
        (100, 10), (100, 50), (100, 100)
    ]

    # Generate samples for each (n, k) pair
    for n, k in specific_pairs:
        plt.figure(figsize=(6, 4))
        means = []  # To store the means of samples for current (n, k)
        std_devs = []  # To store the standard deviations of samples for current (n, k)

        for _ in range(k):
            # Generate a random sample of size n from the data
            sample = np.random.choice(data, size=n, replace=True)
            # Calculate the mean and standard deviation of the sample
            sample_mean = np.mean(sample)
            sample_std_dev = np.std(sample)
            # Append the mean and standard deviation to the lists
            means.append(sample_mean)
            std_devs.append(sample_std_dev)

        # Plot histogram for sample means
        plt.hist(means, bins=20, alpha=0.5)
        plt.xlabel('Mean')
        plt.ylabel('Frequency')
        plt.title(f'Histogram of Sample Means (n={n}, k={k})')
        plt.grid(True)
        plt.show()

        # Plot histogram for sample standard deviations
        plt.hist(std_devs, bins=20, alpha=0.5)
        plt.xlabel('Standard Deviation')
        plt.ylabel('Frequency')
        plt.title(f'Histogram of Sample Standard Deviations (n={n}, k={k})')
        plt.grid(True)
        plt.show()

# Read data from file for Population 1
with open('data1.txt', 'r') as file:
    data1 = [float(line.strip()) for line in file if line.strip()]

print('Population 1 Analysis: ')
# Analyze Population 1
analyze_population(data1, "Data 1")

# Read data from file for Population 2
with open('data2.txt', 'r') as file:
    data2 = [float(line.strip()) for line in file if line.strip()]

print('Population 2 Analysis: ')
# Analyze Population 2
analyze_population(data2, "Data 2")
