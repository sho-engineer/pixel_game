import pyxel
import math
import random

# pyxelの初期設定
pyxel.init(200,200)
pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=5)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=15)

# 3個分のボールの初期設定
ballxs = []
ballys = []
vxs = []
vys = []
for i in range(3):
    ballxs.append(random.randint(0, 199))
    ballys.append(0)
    angle = math.radians(random.randint(30, 150))
    vxs.append(math.cos(angle))
    vys.append(math.sin(angle))

# スコアやスピードなど共通に利用する変数の初期化
gameover = False
speed = 2
padx = 100
score = 0
miss = 0

# 1/30秒ごとに状況を更新する処理の内容
def update():
    global ballxs, ballys, vxs, vys, gameover, speed, padx, score, miss
    # パッドの位置を更新
    padx = pyxel.mouse_x
    # ゲームオーバーになるまで動作
    if gameover == False:
        # ボールの個数分だけボールを移動しボールに関する処理を書く
        for i in range(len(ballxs)):
            ballxs[i] += vxs[i] * speed
            ballys[i] += vys[i] * speed
            # 両端に当たったら左右の進行方向を逆転
            if ballxs[i] >= 200 or ballxs[i] <= 0:
                vxs[i] = -vxs[i]
            # ボールが下端まで行った時の処理
            if ballys[i] >= 200:
                miss += 1
                if miss >= 10:
                    gameover = True
                pyxel.play(0, 1)
                # ボールを上端に移動しx座標や角度を再びランダムに再設定
                ballxs[i] = random.randint(0, 199)
                ballys[i] = 0
                angle = math.radians(random.randint(30, 150))
                vxs[i] = math.cos(angle)
                vys[i] = math.sin(angle)
                # スピード増加（ボールが同時に３個あるとスピードが一気に速くなるので、speedの増加を少し少なくする）
                speed += 0.3
                # （スピードが早すぎるとパッドでキャッチしてもカウントが増えなくなるので最高速を制限する。）
                if speed > 5:
                    speed = 5
            # パッドに当たった時の処理
            if ballys[i] >= 195 and padx - 20 <= ballxs[i] <= padx + 20:
                score += 1
                pyxel.play(0, 0)
                # ボールを上端に移動しx座標や角度を再びランダムに再設定
                ballxs[i] = random.randint(0, 199)
                ballys[i] = 0
                angle = math.radians(random.randint(30, 150))
                vxs[i] = math.cos(angle)
                vys[i] = math.sin(angle)
                # スピード増加
                speed += 0.3
                if speed > 5:
                    speed = 5

# 通常は1/30秒ごとに表示を更新する処理
def draw():
    global ballxs, ballys, gameover, padx, score, miss
    pyxel.cls(7)
    if gameover == True:
        pyxel.text(10, 100, 'Game over!', 0)
    else:
        for i in range(len(ballxs)):
            pyxel.circ(ballxs[i], ballys[i], 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, 'Score: ' + str(score), 0)
    pyxel.text(70, 10, 'Miss: ' + str(miss), 0)

# pyxelの動作を開始
pyxel.run(update, draw)
