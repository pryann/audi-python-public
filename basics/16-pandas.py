from matplotlib import pyplot as plt
import pandas as pd


def get_csv_data(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data, columns=['x_value', 'y_value', 'z_value'])


def calculate_stat_values(data):
    return {
        'min': data.min(),
        'max': data.max(),
        'sum': data.sum(),
        'mean': data.mean(),
        'std': data.std()
    }


def visualize_values(data):
    plt.title('Stat values')
    plt.xlabel('values')
    plt.ylabel('values')
    plt.plot(data)
    plt.text(0, 0, calculate_stat_values(
        df['x_value']), color='#ffffff', backgroundcolor='#000000')
    plt.show()


path = 'files/MOCK_DATA.csv'
df = get_csv_data(path)
print(calculate_stat_values(df['x_value']))
visualize_values(df['x_value'])
