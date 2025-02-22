import tkinter as tk
from tkinter import Canvas
import random

# Функция для создания сердца
def create_heart(canvas, x, y, size, color="red"):
    # Точки для построения сердца
    points = [
        (0, -0.8), (0.25, -1), (0.5, -0.8),
        (0.75, -1), (1, -0.8), (1, -0.3),
        (0.5, 0.5), (0, -0.3)
    ]
    # Масштабируем точки и смещаем их
    scaled_points = [x + px * size for px, py in points for x, y in [(x, y)]]
    return canvas.create_polygon(scaled_points, fill=color, outline=color)

# Инициализация главного окна
root = tk.Tk()
root.title("С 8 марта!")
window_width = 800
window_height = 900
root.geometry(f"{window_width}x{window_height}")

# Создание холста
canvas = Canvas(root, width=window_width, height=window_height, bg="pink")
canvas.pack()

# Переменные для анимации главного сердца
main_heart = None
size_factor = 1
growing = True

# Список для хранения падающих сердец
falling_hearts = []

# Функция для пульсации главного сердца
def pulse_heart():
    global main_heart, size_factor, growing

    if main_heart:
        canvas.delete(main_heart)

    # Увеличиваем или уменьшаем размер сердца
    if growing:
        size_factor += 0.02
        if size_factor >= 1.2:
            growing = False
    else:
        size_factor -= 0.02
        if size_factor <= 0.8:
            growing = True

    # Создаем сердце с новым размером
    main_heart = create_heart(canvas, window_width // 2, window_height // 2 - 50, 200 * size_factor)
    root.after(50, pulse_heart)

# Функция для создания падающих сердец
def create_falling_heart():
    x = random.randint(0, window_width)
    y = -20
    size = random.randint(10, 30)
    color = random.choice(["red", "pink", "purple", "hotpink"])
    heart = create_heart(canvas, x, y, size, color=color)
    falling_hearts.append((heart, y, random.uniform(1, 3)))
    root.after(random.randint(100, 1000), create_falling_heart)

# Функция для анимации падающих сердец
def animate_falling_hearts():
    for i, (heart, y, speed) in enumerate(falling_hearts):
        canvas.move(heart, 0, speed)
        falling_hearts[i] = (heart, y + speed, speed)
        if y > window_height:
            canvas.delete(heart)
            falling_hearts.pop(i)
    root.after(50, animate_falling_hearts)

# Добавляем текст поздравления
canvas.create_text(
    window_width // 2,
    window_height - 50,
    text="С 8 марта!\nС праздником весны и красоты!",
    font=("Arial", 20, "bold"),
    fill="purple",
    justify="center"
)

# Запуск анимаций
pulse_heart()
create_falling_heart()
animate_falling_hearts()

# Запуск главного цикла
root.mainloop()