import pyxel
import math
import random

# pyxelの初期設定
pyxel.init(200,200)
pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=5)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=15)

# ballクラスを定義
class Ball:
    # Ballクラスを初期化
    def __init__(self):
        self.ballx = random.randint(0, 199)
        self.bally = 0
        self.angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(self.angle)
        self.vy = math.sin(self.angle)

    def draw_cirle(self):
        pyxel.circ(self.ballx, self.bally, 10, 6)

# padクラスを定義
class Pad:
    #Padクラスを初期化
    def __init__(self):
        self.padx = 100

# 3個分のボールの初期設定
balls = []
for i in range(3):
    ball = Ball()
    balls.append(ball)

# スコアやスピードなど共通に利用する変数の初期化
gameover = False
speed = 2
score = 0
miss = 0
#Padクラスをインスタン化
pad = Pad()

# 1/30秒ごとに状況を更新する処理の内容
def update():
    global gameover, speed, score, miss

    # パッドの位置を更新
    pad.padx = pyxel.mouse_x
    # ゲームオーバーになるまで動作
    if gameover == False:
        # ボールの個数分だけボールを移動しボールに関する処理を書く
        for b in balls:
            b.ballx += b.vx * speed
            b.bally += b.vy * speed
            # 両端に当たったら左右の進行方向を逆転
            if b.ballx >= 200 or b.ballx <= 0:
                b.vx = -b.vx
            # ボールが下端まで行った時の処理
            if b.bally >= 200:
                miss += 1
                b.bally = 0

                if miss >= 10:
                    gameover = True
                pyxel.play(0, 1)
                # ボールを上端に移動しx座標や角度を再びランダムに再設定
                ball = Ball()
                # スピード増加（ボールが同時に３個あるとスピードが一気に速くなるので、speedの増加を少し少なくする）
                speed += 0.3
                # （スピードが早すぎるとパッドでキャッチしてもカウントが増えなくなるので最高速を制限する。）
                if speed > 5:
                    speed = 5
            # パッドに当たった時の処理
            if b.bally >= 195 and pad.padx - 20 <= b.ballx <= pad.padx + 20:
                score += 1
                b.bally = 0
                pyxel.play(0, 0)
                # ボールを上端に移動しx座標や角度を再びランダムに再設定
                ball = Ball()
                # スピード増加
                speed += 0.3
                if speed > 5:
                    speed = 5

# # 通常は1/30秒ごとに表示を更新する処理
def draw():
    global gameover,score, miss
    pyxel.cls(7)
    if gameover == True:
        pyxel.text(10, 100, 'Game over!', 0)
    else:
        for b in balls:
            b.draw_cirle()
        pyxel.rect(pad.padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, 'Score: ' + str(score), 0)
    pyxel.text(70, 10, 'Miss: ' + str(miss), 0)

# pyxelの動作を開始
pyxel.run(update, draw)
