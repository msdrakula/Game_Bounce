from tkinter import *
import random
import time

tk = Tk()
tk.title("Игра Прыг-Скок!") #Заголовок окна
tk.resizable(0, 0) #Фиксированный размер окна
tk.wm_attributes("-topmost", 1) #Разместить окно по вверх остальных окон
canvas = Canvas(tk, width=500, height=400,bd=0, highlightthickness=0)
canvas.pack()
tk.update()