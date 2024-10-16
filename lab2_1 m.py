import random
from math import cos, sin, pi, sqrt, atan
import matplotlib.pyplot as plt
import time
from datetime import datetime

N = 32 # Кількість точок у сигналі


def generate_signal():
    random.seed(datetime.now().timestamp()) # Ініціалізація генератора випадкових чисел
    signal = []
    for _ in range(N):
        signal.append(random.random()) # Додавання випадкового числа до сигналу

    return signal


# Обчислення коефіцієнтів для k-го члена ряду Фур'є
def calculate_coefficients(k, i, fi):
    return fi*cos(2*pi*k*i/N), fi*sin(2*pi*k*i/N) 

# Обчислення коефіцієнтів A_k та B_k для k-го члена ряду Фур'є.
def calculate_series(k, signal):
    A = 0
    B = 0
    for i in range(N):
        a, b = calculate_coefficients(k, i, signal[i])
        A += a
        B += b
    A = 1/N * A
    B = 1/N * B
    return A, B, 2*(4*N + N + 1)


def plot_graphs(amplitudes, phases):
    plt.figure(figsize=(10, 6))
    plt.stem(range(N), amplitudes, "b", markerfmt="bo",
             basefmt=" ", label="|C_k|")
    plt.title("Спектр амплітуд")
    plt.xlabel("k")
    plt.ylabel("Амплітуда")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.stem(range(N), phases, "b", markerfmt="bo",
             basefmt=" ", label="arg(C_k)")
    plt.title("Спектр фаз")
    plt.xlabel("k")
    plt.ylabel("Амплітуда")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    signal = generate_signal() # Генерація випадкового сигналу
    results = []
    start = time.time() # Початок вимірювання часу

    for k in range(N): 
        results.append(calculate_series(k, signal)) # Обчислення коефіцієнтів для кожного k


    end = time.time() # Кінець вимірювання часу
    print(f"Час обчислення: {end - start}")

    amplitudes = []
    phases = []
    operations = 0

    for A, B, op in results:
        operations += op # Підрахунок загальної кількості операцій
        C = sqrt(A**2 + B**2)/2 # Обчислення амплітуди
        phi = atan(B/A) # Обчислення фази
        amplitudes.append(C)
        phases.append(phi)

    print(f"Кількість операцій множення і додавання: {operations}")
    plot_graphs(amplitudes, phases)


if __name__ == "__main__":
    main()
