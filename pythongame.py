from tkinter import *
import time
import math

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
        if x1 <= 400 or x2 >= WIDTH:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
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

# 이벤트를 처리하는 함수


def fire(event):
    bullets.append(Ball(canvas, 'white', 10, 150, 250, 10, 0))


i = 0
# 윈도우를 생성한다.
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.grid(row=0, column=0, columnspan=2)
canvas.bind('<Button-1>', fire)
l1 = Label(window, text='점수')
l1.grid(row=30, column=10)
e1 = Entry(window)
e1.grid(row=30, column=20)

# 우리 우주선과 외계 우주선을 생성한다.
spaceship = Ball(canvas, 'green', 100, 100, 200, 0, 0)  # 수정하지 말 것!
enemy = Ball(canvas, 'red', 100, 500, 200, 3, 3)        # 수정하지 말 것!

# 리스트에 저장된 각각의 객체를 이동시킨다.
while True:
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

        # 포탄이 화면을 벗어나면 삭제한다.
        if (bullet.x + bullet.size) >= WIDTH:
            canvas.delete(bullet.id)
            bullets.remove(bullet)

    enemy.move()
    window.update()
    time.sleep(0.03)
