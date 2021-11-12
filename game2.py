import pyxel
import math
import random
pyxel.init(200,200)
pyxel.load("game1.py.pyxres")
ballx = [200, 250, 300]
bally = [random.randint(0, 199),random.randint(0, 199), random.randint(0, 199)]
angle = math.radians(random.randint(30, 150))
vx = [-1, -1, -1]
padx = 100
speed = 2
score = 0
miss = 0
pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)
def update():
    global ballx, bally, angle, vx, vy, speed, padx, score, miss
    for i in range(0,3,1):
        ballx[i] += vx[i] * speed
        # bally[i] += vy[i] * speed
        if ballx[i] == 0 and padx-10 < bally[i] < padx+10:
           score += 1
        if ballx[i] <= 0:
           ballx[i] = 200
           bally[i] = random.randint(0, 199)
    padx = pyxel.mouse_y
    if pyxel.btnp(pyxel.KEY_SPACE):
        ballx.append(200)
        bally.append(random.randint(0, 199))
        vx.append(-1)
def draw():
    global ballx, bally, angle, vx, vy, speed, padx, score, miss
    pyxel.cls(12)
    if miss >= 10:
        pyxel.text(80,100,"GAMEOVER",0)
        bally = [0,0,0]
    else:
        a = str(score)
        b = str(miss)
        for t in range(0,3,1):
            #pyxel.circ(ballx[t], bally[t], 10, 6)
            pyxel.blt(ballx[t], bally[t], 0, 0, 0, 15, 15)
        #pyxel.rect(0, padx, 40, 5, 14)
        pyxel.blt(0, padx, 0, 32, 0, 15, 15)
        pyxel.text(10,10,"score:",0)
        pyxel.text(40,10,a,0)
        pyxel.text(10,20,"drop:",0)
        pyxel.text(40,20,b,0)
pyxel.run(update, draw)
