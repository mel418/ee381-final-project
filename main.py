import numpy as np
import matplotlib.pyplot as plt

def analyze_population(data, population_name):
    mean = np.mean(data)
    std_dev = np.std(data)
    sort = np.sort(data)

    # Plot histogram for original data
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {population_name}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"Mean of {population_name}:", mean)
    print(f"Standard Deviation of {population_name}:", std_dev)

    # Plot the sorted data
    plt.plot(sort)
    plt.title(f'{population_name} Sorted Data')
    plt.xlabel('n')
    plt.ylabel('x')
    plt.show()


    # (n, k) pairs
    specific_pairs = [
        (10, 10), (10, 50), (10, 100),
        (50, 10), (50, 50), (50, 100),
        (100, 10), (100, 50), (100, 100)
    ]

    print("\nCalculated Values:")
    print("n\tk\tE(x_bar)\tS(x_bar)\tE(s)")
    
    # samples for each (n, k) pair
    for i, (n, k) in enumerate(specific_pairs):
        means = []  # means of samples for current (n, k)
        std_devs = []  # standard deviations of samples for current (n, k)

        for _ in range(k):
            sample = np.random.choice(data, size=n, replace=False)
            sample_mean = np.mean(sample)
            sample_std_dev = np.std(sample)
            means.append(sample_mean)
            std_devs.append(sample_std_dev)

        # Calculate statistics for the specific (n, k) pair
        expected_mean = np.mean(means)
        expected_std_dev_of_means = np.std(means)
        expected_std_dev = np.mean(std_devs)

        # Plot histograms for sample means and sample standard deviations in the same figure
        plt.figure(figsize=(12, 6))

        # Histogram of sample means
        plt.subplot(1, 2, 1)
        plt.hist(means, bins=30, edgecolor='black', alpha=0.5, color='skyblue')
        plt.xlabel('x_bar')
        plt.ylabel('Frequency')
        plt.title(f'Sample Means\nE(x_bar)={expected_mean:.2f}, S(x_bar)={expected_std_dev_of_means:.2f}')
        plt.grid(True)

        # Histogram of sample standard deviations
        plt.subplot(1, 2, 2)
        plt.hist(std_devs, bins=30, edgecolor='black', alpha=0.5, color='orange')
        plt.xlabel('S')
        plt.ylabel('Frequency')
        plt.title(f'Sample Standard Deviations (n={n}, k={k})\nE(s)={expected_std_dev:.2f}')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        print(f"{n}\t{k}\t{expected_mean}\t{expected_std_dev_of_means}\t{expected_std_dev}")

# Read data from file for Population 1
with open('data1.txt', 'r') as file:
    data1 = [float(line.strip()) for line in file if line.strip()]

print('Population 1 Analysis: ')
analyze_population(data1, "Data 1")

# Read data from file for Population 2
with open('data2.txt', 'r') as file:
    data2 = [float(line.strip()) for line in file if line.strip()]

print('Population 2 Analysis: ')
analyze_population(data2, "Data 2")
