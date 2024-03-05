import tkinter as tk
from time import strftime
import math

def update_time():
    draw_clock_hands()
    canvas.after(1000, update_time)

def draw_clock_hands():
    canvas.delete("all")

    center_x = 150
    center_y = 150
    radius = 80

    current_time = strftime('%H:%M:%S %p')

    time_now = strftime('%H:%M:%S')
    hours, minutes, seconds = map(int, time_now.split(':'))

    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='white', width=4)

    second_angle = math.radians(6 * seconds)
    draw_hand(center_x, center_y, second_angle, 70, "red")

    minute_angle = math.radians(6 * minutes + 0.1 * seconds)
    draw_hand(center_x, center_y, minute_angle, 60, "white")

    hour_angle = math.radians(30 * hours + 0.5 * minutes)
    draw_hand(center_x, center_y, hour_angle, 50, "white")

def draw_hand(center_x, center_y, angle, length, color):
    x = center_x + length * math.sin(angle)
    y = center_y - length * math.cos(angle)
    canvas.create_line(center_x, center_y, x, y, width=3, fill=color)

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=300, height=300, bg='black')
canvas.pack()
canvas.create_oval(10, 10, 290, 290, outline='white', width=2)

update_time()

root.mainloop()