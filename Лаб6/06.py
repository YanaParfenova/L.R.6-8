"""
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению
в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов) и целевую функцию
для нахождения оптимального  решения.

Вариант 17. В группе N человек. Сформировать все возможные варианты разбиения
группы на подгруппы  при условии, что в подгруппу входит не более 10 человек.
"""


import itertools
import timeit

# Алгоритмический способ формирования разбиений.
def generate_partitions_algorithmic(n):
   
    if n == 0:
        return [[]]
    result = []
    for i in range(1, min(n, 10) + 1):
        for partition in generate_partitions_algorithmic(n - i):
            result.append([[i]] + partition)
    return result

# Использование встроенных функций Python для формирования разбиений.
def generate_partitions_python(n):
    
    def partitions(n):
        if n == 0:
            yield []
        for i in range(1, min(n, 10) + 1):
            for p in partitions(n - i):
                yield [i] + p

    return list(partitions(n))

# Измерение времени выполнения
N = int(input("Введите количесто человек в группе(n):"))

# Алгоритмический способ
start_time_algo = timeit.default_timer()
partitions_algo = generate_partitions_algorithmic(N)
end_time_algo = timeit.default_timer()

# Способ с использованием функций Python
start_time_func = timeit.default_timer()
partitions_func = generate_partitions_python(N)
end_time_func = timeit.default_timer()

# Вывод результатов
print(f"Количество разбиений (алгоритмический способ): {len(partitions_algo)}")
print(f"Время выполнения (алгоритмический способ): {end_time_algo - start_time_algo:.6f} секунд")

print(f"Количество разбиений (функции Python): {len(partitions_func)}")
print(f"Время выполнения (функции Python): {end_time_func - start_time_func:.6f} секунд")


# Алгоритмический способ формирования разбиений с ограничением по количеству подгрупп.
def generate_partitions_with_limit_algo(n, max_groups):
    
    if n == 0:
        return [[]]
    result = []
    for i in range(1, min(n, 10) + 1):
        for partition in generate_partitions_with_limit_algo(n - i, max_groups - 1):
            if len(partition) < max_groups - 1:  # Проверка на количество подгрупп
                result.append([[i]] + partition)
    return result

# Использование встроенных функций Python для формирования разбиений с ограничением по количеству подгрупп.
def generate_partitions_with_limit_python(n, max_groups):
    
    def partitions(n, max_groups):
        if n == 0:
            yield []
        if max_groups <= 0:
            return
        for i in range(1, min(n, 10) + 1):
            for p in partitions(n - i, max_groups - 1):
                if len(p) < max_groups - 1:
                    yield [i] + p

    return list(partitions(n, max_groups))


max_groups = int(input("Введите максимальное количесто подгрупп:"))  # Максимальное количество подгрупп

# Алгоритмический способ
start_time_algo = timeit.default_timer()
partitions_algo = generate_partitions_with_limit_algo(N, max_groups)
end_time_algo = timeit.default_timer()

# Способ с использованием функций Python
start_time_func = timeit.default_timer()
partitions_func = generate_partitions_with_limit_python(N, max_groups)
end_time_func = timeit.default_timer()


# Вывод результатов
print(f"Количество разбиений с ограничением по количеству подгрупп (алгоритмический способ): {len(partitions_algo)}")
print(f"Время выполнения (алгоритмический способ): {end_time_algo - start_time_algo:.6f} секунд")

print(f"Количество разбиений с ограничением по количеству подгрупп (функции Python): {len(partitions_func)}")
print(f"Время выполнения (функции Python): {end_time_func - start_time_func:.6f} секунд")


