"""
Требуется для своего варианта второй части л.р. №6 (усложненной программы)
разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
Вариант 17. В группе N человек. Сформировать все возможные варианты
разбиения группы на подгруппы  при условии, что в подгруппу входит
не более 10 человек.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import timeit

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


def show_partitions():
    try:
        n = int(entry_people.get())  # Количество человек
        max_groups = int(entry_groups.get())  # Максимальное количество подгрупп
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные целые числа.")
        return

    # Алгоритмический способ
    start_time_algo = timeit.default_timer()
    partitions_algo = generate_partitions_with_limit_algo(n, max_groups)
    end_time_algo = timeit.default_timer()

    # Способ с использованием функций Python
    start_time_func = timeit.default_timer()
    partitions_func = generate_partitions_with_limit_python(n, max_groups)
    end_time_func = timeit.default_timer()

    # Создаем окно для вывода
    output_window = tk.Toplevel(root)
    output_window.title("Результаты разбиений")
    output_window.geometry("400x300")

    # Установка позиции окна по центру экрана
    screen_width = output_window.winfo_screenwidth()
    screen_height = output_window.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (300 // 2)
    output_window.geometry(f"400x300+{x}+{y}")

    # Текстовое поле для вывода результатов с прокруткой
    output_text = scrolledtext.ScrolledText(output_window, width=50, height=15)
    output_text.pack(padx=10, pady=10)

    # Вывод результатов
    output_text.insert(tk.END, "Алгоритмический способ:\n" + str(partitions_algo) + "\n\n")
    output_text.insert(tk.END, "Способ с использованием функций Python:\n" + str(partitions_func) + "\n\n")
    output_text.insert(tk.END, f"Время алгоритмического метода: {end_time_algo - start_time_algo:.6f} секунд\n")
    output_text.insert(tk.END, f"Время метода с использованием функций Python: {end_time_func - start_time_func:.6f} секунд\n")


# Основное окно приложения
root = tk.Tk()
root.title("Генератор разбиений")
root.geometry("300x200")

# Установка позиции окна по центру экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (300 // 2)
y = (screen_height // 2) - (200 // 2)
root.geometry(f"300x200+{x}+{y}")

# Поля ввода
label_people = tk.Label(root, text="Введите количество человек (n):")
label_people.pack(pady=5)

entry_people = tk.Entry(root)
entry_people.pack(pady=5)

label_groups = tk.Label(root, text="Введите максимальное количество подгрупп:")
label_groups.pack(pady=5)

entry_groups = tk.Entry(root)
entry_groups.pack(pady=5)

btn_generate = tk.Button(root, text="Сгенерировать", command=show_partitions)
btn_generate.pack(pady=20)

root.mainloop()
