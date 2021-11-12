import pyxel
import math
import random

# setup
vx = [-1, -1, -1]
padx = 100
speed = 2
speed1 = 1
score = 0
range = range(0,3,1)
ballx = [200, 250, 300]
bally = [random.randint(0, 199),random.randint(0, 199), random.randint(0, 199)]
angle = math.radians(random.randint(30, 150))
rAppleX = [200, 250, 300]
rAppleY = [random.randint(0, 199),random.randint(0, 199), random.randint(0, 199)]


# アプリ全体
class App:
    def __init__(self):
        # 画面表示
        pyxel.init(200, 200)
        # human()/apple()/rottenApple()のインスタンスを作成
        self.human = human()
        self.apple = apple()
        self.rottenApple = rottenApple()
        # pyxel.load("game1.py.pyxres")
        # pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
        # pyxel.sound(1).set(note='C2', tone='T', volume='3', effect='N', speed=30)

        # Appを起動
        pyxel.run(self.update, self.draw)

    def update(self):
        global ballx, bally, vx, speed, score, padx, rAppleX, rAppleY
        # りんごをふらす
        # ballはりんご・rAppleは腐ったりんご
        for i in range:
            # りんごと腐ったりんごを降らせる
            ballx[i] += vx[i] * speed
            rAppleX[i] += vx[i] * speed1
            # りんごを拾ったらスコアを追加
            if ballx[i] == 0 and padx-10 < bally[i] < padx+10:
               score += 1
               ballx[i] = 200
            # 腐ったりんごを拾うとスコアマイナス
            if rAppleX[i] == 0 and padx-10 < rAppleY[i] < padx+10:
               score -= 1

            # 境界条件
            if ballx[i] < -4:
                 ballx[i] = 200
            if rAppleX[i] < -10:
                rAppleX[i] = 200

            if ballx[i] <= -4:
                score -= 1

        if pyxel.btnp(pyxel.KEY_SPACE):
            ballx.append(200)
            bally.append(random.randint(0, 199))
            vx.append(-1)
    def draw(self):
        global ballx, bally, angle, vx, vy, speed, padx, score,a
        # 背景色設定
        pyxel.cls(12)
        # インスタンスのdrawを起動
        self.apple.draw()
        self.rottenApple.draw()
        self.human.draw()
        # ゲームオーバー
        if score <= -1:
             pyxel.text(80,100,"GAMEOVER",0)
             bally = [0,0,0]
        else:
             a = str(score)

        pyxel.text(10,10,"score:",0)
        pyxel.text(40,10,a,0)

# りんご
class apple:
        def __init__(self):
            pass
        def update(self):
            pass
        def draw(self):
            # りんごを描写
            global ballx, bally
            for t in range:
                    pyxel.blt(ballx[t], bally[t], 0, 0, 0, 15, 15)

# 人間
class human:
        def __init__(self):
            pass
        def update(self):
             pass
        def draw(self):
            # 人間を描写
            global padx
            padx = pyxel.mouse_y
            pyxel.blt(0, padx, 0, 32, 0, 15, 15)

# 腐ったりんご
class rottenApple:
        def __init__(self):
            pass
        def update(self):
            pass
        def draw(self):
            # 腐ったりんごを描写
            global rAppleX,rAppleY
            for t in range:
                    pyxel.blt(rAppleX[t], rAppleY[t], 0, 0,30, 10, 10)
App()
apple()
human()
rottenApple()
