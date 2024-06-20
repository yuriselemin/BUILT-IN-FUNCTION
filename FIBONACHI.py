
# Генератор фибоначи


# Функция для генерации чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создание генератора чисел Фибоначчи
fib_generator = fibonacci()

# Вывод первых 10 чисел Фибоначчи
for i in range(20):
    print(next(fib_generator))





