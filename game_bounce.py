from tkinter import *
import random
import time

class Ball: # Мяч
	def __init__(self,canvas, color): # canvas -холст, color- цвет
		self.canvas = canvas
		self.id = canvas.create_oval(10,10, 25, 25, fill=color) # вызываем функцию create_oval для рисования круга, id идентификатор круга
		self.canvas.move(self.id, 245, 100) #Перемещаем круг по координатам
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()

	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id) #Возвращает координаты в виде списка из 4 чисел
		if pos[1] <= 0:
			self.y = 1
		if pos[3] >= self.canvas_height:
			self.y = -1
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3

class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0 , 100, 10, fill=color)
		self.canvas.move(self.id, 200, 300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0

		elif pos[2] >= self.canvas_width:
			self.x = 0

	def turn_left(self, evt):
		self.x = -2

	def turn_right(self, evt):
		self.x = 2








tk = Tk()
tk.title("Игра Прыг-Скок!") #Заголовок окна
tk.resizable(0, 0) #Фиксированный размер окна
tk.wm_attributes("-topmost", 1) #Разместить окно по вверх остальных окон
canvas = Canvas(tk, width=500, height=400,bd=0, highlightthickness=0)
canvas.pack() #При вызове холст изменит размер в соответствии со значениями ширины и высоты
tk.update()

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, 'red')

while 1: #Главный цикл программы
	ball.draw()
	paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
