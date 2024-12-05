"""
Требуется написать ООП с графическим интерфейсом в соответствии со своим
вариантом. Должны быть реализованы минимум один класс, три атрибута,
четыре метода (функции). Ввод данных из файла с контролем правильности ввода.
Базы данных не использовать. При необходимости сохранять информацию
в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
Для GUI и визуализации использовать библиотеку tkinter.

Вариант 17
Объекты – ромбы
Функции:
проверка пересечения
визуализация
раскраска
поворот вокруг заданной точки окружности

"""

import tkinter as tk
from tkinter import messagebox
import math

class Romb:
    def __init__(self, x_center, y_center, width, height, color="blue"):
        self.x_center = x_center
        self.y_center = y_center
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0

# Возвращает координаты вершин ромба.
    def get_vertices(self):        
        x0 = self.x_center
        y0 = self.y_center
        half_width = self.width / 2
        half_height = self.height / 2
        return [
            (x0, y0 - half_height),  # верхняя вершина
            (x0 + half_width, y0),  # правая вершина
            (x0, y0 + half_height),  # нижняя вершина
            (x0 - half_width, y0)   # левая вершина
        ]

# Поворачивает ромб вокруг центра.
    def rotate(self, angle):
        self.angle += angle
        self.angle %= 360

# Возвращает координаты вершин ромба после поворота.
    def get_rotated_vertices(self):
        angle_rad = math.radians(self.angle)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)
        vertices = self.get_vertices()
        rotated_vertices = []
        for (x, y) in vertices:
            x_rotated = self.x_center + (x - self.x_center) * cos_angle - (y - self.y_center) * sin_angle
            y_rotated = self.y_center + (x - self.x_center) * sin_angle + (y - self.y_center) * cos_angle
            rotated_vertices.append((x_rotated, y_rotated))
        return rotated_vertices

class RombApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Работа с Ромбами")

        self.canvas = tk.Canvas(master, bg="white", width=400, height=400)
        self.canvas.pack()

        self.rombs = []  # Список для хранения всех ромбов

        self.color_button = tk.Button(master, text="Раскрасить", command=self.change_color)
        self.color_button.pack(side=tk.LEFT)

        self.rotate_button = tk.Button(master, text="Повернуть", command=self.rotate_romb)
        self.rotate_button.pack(side=tk.LEFT)

        self.check_button = tk.Button(master, text="Проверка пересечения", command=self.check_intersection)
        self.check_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(master, text="Визуализация", command=self.load_data)
        self.load_button.pack(side=tk.LEFT)

    def visualize(self):
        self.canvas.delete("all")
        for romb in self.rombs:
            vertices = romb.get_rotated_vertices()
            self.canvas.create_polygon(vertices, fill=romb.color, outline="black")

# Изменяем цвет для каждого ромба
    def change_color(self):        
        for romb in self.rombs:
            romb.color = "red" if romb.color == "blue" else "blue"
        self.visualize()

# Поворачиваем каждый ромб на 15 градусов
    def rotate_romb(self):
        for romb in self.rombs:
            romb.rotate(15)
        self.visualize()

        
# Проверка пересечения между ромбами
    def check_intersection(self):
        for i in range(len(self.rombs)):
            for j in range(i + 1, len(self.rombs)):
                if self.check_if_intersect(self.rombs[i], self.rombs[j]):
                    messagebox.showinfo("Проверка пересечения", f"Ромбы {i + 1} и {j + 1} пересекаются.")

    def load_data(self):
        try:
            with open("romb_data.txt", "r") as f:
                self.rombs.clear()
                for line in f:
                    data = line.strip().split()
                    if len(data) != 5:
                        raise ValueError("Неверное количество данных.")
                    x_center, y_center, width, height, color = map(str, data)
                    x_center, y_center, width, height = map(float, [x_center, y_center, width, height])
                    self.rombs.append(Romb(x_center, y_center, width, height, color))
                self.visualize()
        except Exception as e:
            messagebox.showerror("Ошибка загрузки", str(e))

# Проверка на пересечение между двумя ромбами.
    def check_if_intersect(self, romb1, romb2):
        vertices1 = romb1.get_rotated_vertices()
        vertices2 = romb2.get_rotated_vertices()

        def in_range(p, box):
            return box[0] <= p[0] <= box[2] and box[1] <= p[1] <= box[3]

        min_x1 = min(v[0] for v in vertices1)
        max_x1 = max(v[0] for v in vertices1)
        min_y1 = min(v[1] for v in vertices1)
        max_y1 = max(v[1] for v in vertices1)

        min_x2 = min(v[0] for v in vertices2)
        max_x2 = max(v[0] for v in vertices2)
        min_y2 = min(v[1] for v in vertices2)
        max_y2 = max(v[1] for v in vertices2)

        return not (max_x1 < min_x2 or max_x2 < min_x1 or max_y1 < min_y2 or max_y2 < min_y1)
    
root = tk.Tk()
root.geometry("450x450")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (450 // 2)
root.geometry(f"450x450+{x}+{y}")

app = RombApp(root)
root.mainloop()

    
