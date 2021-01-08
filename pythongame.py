from tkinter import *
import time
import math
import random

WIDTH = 800
HEIGHT = 400


class Ball:
    def __init__(self, canvas, color, size, x, y, xspeed, yspeed):
        self.canvas = canvas      # 캔버스 객체
        self.color = color      # Ball의 색상
        self.size = size      # Ball의 크기
        self.x = x         # Ball의 x좌표
        self.y = y         # Ball의 y좌표
        self.xspeed = xspeed      # Ball의 수평방향 속도
        self.yspeed = yspeed      # Ball의 수직방향 속도
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color)

    def move(self):         # Ball을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)   # 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 300 or x2 >= WIDTH:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.xspeed = - self.xspeed      # 속도의 부호를 반전시킨다.
        if y1 <= 0 or y2 >= HEIGHT:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.yspeed = - self.yspeed      # 속도의 부호를 반전시킨다.

    def bul_move(self):         # Bullet을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)   # 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.xspeed = - self.xspeed      # 속도의 부호를 반전시킨다.
        if y1 <= 0 or y2 >= HEIGHT:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.yspeed = - self.yspeed      # 속도의 부호를 반전시킨다.


# 생성된 포탄을 저장하는 리스트
bullets = []
lengths = []

chance = 0


def fire(event):  # 이벤트를 처리하는 함수
    global chance
    bullets.append(Ball(canvas, 'white', 10, 150, 250, 15, 0))
    chance += 1


paused = True


paused_check = ["True"]


def is_paused(event):
    global paused
    if paused == True:
        paused = False
        global paused_check
        if len(paused_check) > 0:
            paused_check = []
        paused_check.append("False")
        print('f')
    else:
        paused = True
        if len(paused_check) > 0:
            paused_check = []
        paused_check.append("True")
        print('t')


def go():
    time.sleep(1)


def stop():
    time.sleep(1)


i = 0
# 윈도우를 생성한다.
window = Tk()
window.title('GreenShooter')  # 우리 게임 이름 정함
window.resizable(False, False)  # 게임창 사이즈 임의로 못바꾸게
canvas = Canvas(window, width=WIDTH, height=HEIGHT, relief='solid', bd=2)
canvas.grid(row=0, column=0, columnspan=1)
canvas.bind('<Button-1>', fire)
l1 = Label(window, text='점수', fg='green', relief='groove')
l1.grid(row=1, column=2)
l2 = Label(window, text='총알', fg='green', relief='groove')
l2.grid(row=2, column=2)
e1 = Entry(window)
e1.grid(row=1, column=3)
e2 = Entry(window)
e2.grid(row=2, column=3)
b2 = Button(window, text='go', command=go, relief='groove')
b2.grid(row=3, column=2)
b1 = Button(window, text='stop for 2sec', command=stop, relief='groove')
b1.grid(row=3, column=3)
canvas.bind('<Button-3>', is_paused)

# 우리 우주선과 외계 우주선을 생성한다.
a = random.randrange(30, 100)/10
b = random.randrange(30, 100)/10
spaceship = Ball(canvas, 'green', 100, 100, 200, 0, 0)
enemy = Ball(canvas, 'red', 100, 500, 200, a, b)

# 리스트에 저장된 각각의 객체를 이동시킨다.
while True:
    # canvas.bind('<Button-3>', is_paused)
    while True:
        if paused_check[0] == "True":
            paused = True
            print("True")
            break
        elif paused_check[0] == "False":
            paused = False
            print("False")
            break
    if paused:
        for bullet in bullets:
            bullet.bul_move()
            (a, b) = (bullet.x+5, bullet.y+5)
            (c, d) = (enemy.x+50, enemy.y+50)
            length = ((a-c)**2+(b-d)**2)**0.5
            lengths.append(length)
            if length <= 55:
                canvas.delete(bullet.id)
                bullets.remove(bullet)
                i += 1
                e1.delete(0, END)
                e1.insert(0, i)
                e2.delete(0, END)
                e2.insert(0, 20-chance)

            # 포탄이 화면을 벗어나면 삭제한다.
            if (bullet.x + bullet.size) >= WIDTH:
                canvas.delete(bullet.id)
                bullets.remove(bullet)
        enemy.move()
        time.sleep(0.03)
        if chance == 21:
            break
    window.update()
