import numpy as np
import matplotlib.pyplot as plt

def analyze_population(data, population_name):
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data)

    # Plot histogram
    plt.hist(data, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Population')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {population_name}')
    plt.grid(True)
    plt.show()

    print("Mean:", mean)
    print("Standard Deviation:", std_dev)

    # Define the specific (n, k) pairs
    specific_pairs = [
        (10, 10), (10, 50), (10, 100),
        (50, 10), (50, 50), (50, 100),
        (100, 10), (100, 50), (100, 100)
    ]

    # Generate samples for each (n, k) pair
    sample_means = []  # To store the means of each sample
    sample_std_devs = []  # To store the standard deviations of each sample
    n_values = []  # To store the values of n used in the samples

    for n, k in specific_pairs:
        n_values.append(n)
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

        # Append the means and standard deviations for current (n, k) to the main lists
        sample_means.append(means)
        sample_std_devs.append(std_devs)

    # Calculate statistics for the specific (n, k) pairs
    specific_means = []  # To store the expected means (E(x_bar))
    specific_std_devs_of_means = []  # To store the standard deviations of the means (S(x_bar))
    specific_std_devs = []  # To store the expected standard deviations (E(s))

    for means, std_devs in zip(sample_means, sample_std_devs):
        # Calculate the mean of sample means
        expected_mean = np.mean(means)
        # Calculate the standard deviation of sample means
        expected_std_dev_of_means = np.std(means)
        # Calculate the mean of standard deviations
        expected_std_dev = np.mean(std_devs)

        # Append the calculated values to the lists
        specific_means.append(expected_mean)
        specific_std_devs_of_means.append(expected_std_dev_of_means)
        specific_std_devs.append(expected_std_dev)

    # Plot histograms for mean values and standard deviations
    plt.figure(figsize=(12, 6))

    # Histogram for mean values
    plt.subplot(1, 2, 1)
    for i, (n, k) in enumerate(specific_pairs):
        plt.hist(sample_means[i], bins=20, alpha=0.5, label=f'n={n}, k={k}')
    plt.xlabel('Mean')
    plt.ylabel('Frequency')
    plt.title('Histogram of Sample Means')
    plt.legend()

    # Histogram for standard deviations
    plt.subplot(1, 2, 2)
    for i, (n, k) in enumerate(specific_pairs):
        plt.hist(sample_std_devs[i], bins=20, alpha=0.5, label=f'n={n}, k={k}')
    plt.xlabel('Standard Deviation')
    plt.ylabel('Frequency')
    plt.title('Histogram of Sample Standard Deviations')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Print the calculated values in tabular format
    print("n\tk\tE(x_bar)\tS(x_bar)\tE(s)")
    for i, (n, k) in enumerate(specific_pairs):
        print(f"{n}\t{k}\t{specific_means[i]}\t{specific_std_devs_of_means[i]}\t{specific_std_devs[i]}")

# Read data from file for Population 1
with open('data1.txt', 'r') as file:
    data1 = [float(line.strip()) for line in file if line.strip()]

print('Population 1 Analysis: ')
# Analyze Population 1
analyze_population(data1, "Population 1")

# Read data from file for Population 2
with open('data2.txt', 'r') as file:
    data2 = [float(line.strip()) for line in file if line.strip()]

print('Population 2 Analysis: ')
# Analyze Population 2
analyze_population(data2, "Population 2")
