import pandas as pd
import matplotlib.pyplot as plt


def dict_to_dataframe(data_dict):
    """Преобразования словаря с временем работы алгоритмов в pandas DataFrame."""
    data = []
    for alg, times in data_dict.items():
        for size, time in times.items():
            data.append({'Алгоритм': alg, 'Количество данных': size, 'Время работы (мс)': time})
    # Создание DataFrame
    df = pd.DataFrame(data)
    return df


def plot_data(df):
    """Построение графика времени работы алгоритмов на основе DataFrame"""
    fig, ax = plt.subplots()
    for algorithm in df['Алгоритм'].unique():
        alg_data = df[df['Алгоритм'] == algorithm]
        ax.plot(alg_data['Количество данных'], alg_data['Время работы (мс)'], label=algorithm, marker='o')
    ax.set_xlabel('Количество данных')
    ax.set_ylabel('Время работы (мс)')
    ax.legend()
    plt.show()

