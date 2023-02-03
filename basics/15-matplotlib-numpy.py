from matplotlib import pyplot as plt
import numpy as np


def get_csv_data(path):
    return np.loadtxt(path, delimiter=',', dtype=float,
                      skiprows=1, usecols=np.arange(3, 6))


def calculate_stat_values(arr):
    return {
        'min': np.min(arr),
        'max': np.max(arr),
        'sum': np.sum(arr),
        'mean': np.mean(arr),
        'std': np.std(arr)
    }


def visualize_values(data):
    plt.title('Stat values')
    plt.xlabel('values')
    plt.ylabel('values')
    plt.plot(data)
    plt.show()


path = 'files/MOCK_DATA.csv'
arr = get_csv_data(path)
print(calculate_stat_values(arr[:, 0]))
visualize_values(arr[:, 0])
