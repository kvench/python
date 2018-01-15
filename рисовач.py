from tkinter import *
import random
# создаем прямоульник
tk = Tk()
c = Canvas(tk, width=640, height=640, bg='white')
c.pack()
ovalxspeed = []
ovalyspeed = []
# выделяем скорость шарика в переменные
my_rect = c.create_rectangle(130, 630, 230, 640, fill='blue')
x1, y1, x2, y2 = c.coords(my_rect)
def keyDown(key):
    x1, y1, x2, y2 = c.coords(my_rect)
    if key.char == 'a':
        # сдвигаем прямоугольник влево
        if x1 > 0:
            c.move(my_rect, -20, 0)

    # если нажали d
    if key.char == 'd':
         if x2 < 640:
        # сдвигаем прямоугольник вправо
            c.move(my_rect, 20, 0)


# при нажатии любой клавишы вызываем keyDown
tk.bind("<KeyPress>", keyDown)

numbers = []
for i in range(1):
    my_favorite_oval = c.create_oval(10, 10, 50, 50, fill='blue')
    numbers.append(my_favorite_oval)
for i in range(1):
    ovalxspeed.append(random.randint(10, 30))
    ovalyspeed.append(random.randint(10, 30))


# сохраняем номер созданной фигуры в переменную


def moveBall():
    # используем переменные vx и vy, как глобальные
    global ovalxspeed, ovalyspeed

    for i in range(1):
        x1, y1, x2, y2 = c.coords(numbers[i])

        

        # аналогично по y
        if y1 <= 0 or y2 >= 640:
            ovalyspeed[i] *= -1

        # передвигаем наш овал на скорость
        c.move(numbers[i], ovalxspeed[i], ovalyspeed[i])
    # повторяем через полсекунды
    c.after(50, moveBall)

# спустя полсекунды (50 мс) после запуска выполнить moveBall
c.after(50, moveBall)

mainloop()
