import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначаємо функцію та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створюємо діапазон значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створюємо графік
fig, ax = plt.subplots()

# Малюємо функцію
ax.plot(x, y, 'r', linewidth=2)

# Заповнюємо область під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштовуємо графік
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додаємо межі інтегрування та назву графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
N = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
under_curve = y_random < f(x_random)
monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / N

print("Інтеграл методом Монте-Карло: ", monte_carlo_integral)

# Перевіряємо за допомогою функції quad
quad_integral, error = spi.quad(f, a, b)
print("Інтеграл за допомогою quad: ", quad_integral)
print("Абсолютна помилка: ", error)
