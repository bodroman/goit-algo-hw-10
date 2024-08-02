import pulp

# Створюємо модель
model = pulp.LpProblem("Optimization_Production", pulp.LpMaximize)

# Змінні для кількості вироблених одиниць лимонаду та фруктового соку
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat='Continuous')

# Об'єктивна функція: максимізує загальну кількість вироблених напоїв
model += lemonade + fruit_juice

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100  # вода
model += 1 * lemonade <= 50  # цукор
model += 1 * lemonade <= 30  # лимонний сік
model += 2 * fruit_juice <= 40  # фруктове пюре

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонадів для виробництва: {lemonade.varValue}")
print(f"Кількість фруктових соків для виробництва: {fruit_juice.varValue}")
print(f"Максимальний загальний обсяг виробництва: {pulp.value(model.objective)}")
