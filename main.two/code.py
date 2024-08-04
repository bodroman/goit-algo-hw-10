import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return np.sin(x)

def monte_carlo_integral(f, a, b, N=100000):

    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, 1, N)
    under_curve = y_random < f(x_random)
    return (b - a) * 1 * np.sum(under_curve) / N

# Визначення меж інтегрування
a = 0  # Нижня межа
b = np.pi  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
monte_carlo_integral_value = monte_carlo_integral(f, a, b)
print("Інтеграл методом Монте-Карло: ", monte_carlo_integral_value)

# Перевірка за допомогою функції quad
quad_integral, error = spi.quad(f, a, b)
print("Інтеграл за допомогою quad: ", quad_integral)
print("Абсолютна помилка: ", error)
