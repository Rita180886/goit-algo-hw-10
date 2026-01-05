import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

def monte_carlo_integral(f, a, b, n_points=10000):
    x_rand = np.random.uniform(a, b, n_points)
    y_rand = f(x_rand)
    return (b - a) * np.mean(y_rand)

def plot_integral(f, a, b):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b, 200)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.5])

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')

    ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")

    plt.grid(True)
    plt.show()

def main():
    a = 0.0
    b = 2.0
    
    n_points = 10000

    mc_result = monte_carlo_integral(f, a, b, n_points)

    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Межі інтегрування: [{a}, {b}]")
    print(f"Кількість точок для Монте-Карло: {n_points}")
    print()

    print(f"Результат методом Монте-Карло: {mc_result:.6f}")
    print(f"Результат функції quad:       {quad_result:.6f}")
    print(f"Оцінка похибки quad:          {quad_error:.2e}")
    print(f"Різниця між результатами:     {abs(mc_result - quad_result):.6f}")

    plot_integral(f, a, b)

if __name__ == "__main__":
    main()