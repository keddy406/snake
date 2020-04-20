import pygame, sys
from pygame.locals import *
import time
import random
def main():
    pygame.init()
    pygame.display.set_caption('拉機貪食蛇')
    screen = pygame.display.set_mode((600,600))
    bgSong = pygame.mixer.Sound("bg.wav")
    eatSong = pygame.mixer.Sound("icebird.wav")
    endSong = pygame.mixer.Sound('flash.wav')
    bgSong.play(-1)
    class Snake():
        def __init__(self):
            self.x = 0
            self.y = 300
            self.size = 20
            self.headColor = [255, 255, 0]
            self.bodyColor = [255, 255, 255]
            self.direction = 'right'
            #初始化樹至四個長方形為蛇身
            self.body =[]
            self.eat = False
            for x in range(4):
                self.body.append(Rect(self.x, self.y))
                self.y += 20
            #為了之後蛇前進的初始位置
            self.y =300

        def draw(self):
            #改變蛇頭顏色
            self.body[0].color = self.headColor
            for b in range(1,len(self.body)):
                self.body[b].color = self.bodyColor
            for n in range(len(self.body)-1, -1, -1):
                self.body[n].draw()

        def step(self):
            #設置方向 蛇的移動
            if snake.direction == 'top':
                self.y -= 20
            elif self.direction == 'down':
                self.y += 20
            elif self.direction == 'left':
                self.x -= 20
            elif self.direction =='right':
                self.x += 20
            #創建rect 對象插入數組中
            self.body.insert(0, Rect(self.x, self.y))
            #殺除最後一項
            if not self.eat:
                self.body.pop()
            else:
                self.eat = False
#設置長方形 方便產生蛇身
    class Rect():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.color = [255, 255, 255]
        def draw(self):
            pygame.draw.rect(screen, self.color, [self.x, self.y, 20, 20], 0)
            pygame.draw.rect(screen, [0, 0, 0], [self.x, self.y, 20, 20], 1)

    class Food():
        #實例化食物
        def __init__(self):
            self.x = random.randrange(0, 600, 20)
            self.y = random.randrange(0, 600, 20)
            self.foodColor =[0, 100, 255]
        def draw(self):
            pygame.draw.rect(screen, self.foodColor, [self.x, self.y, 20, 20], 0)

    def checkHit():
        global score
        if snake.body[0].x == food.x and snake.body[0].y == food.y:
            snake.eat = True
            score += 1
            food.x = random.randrange(0, 600, 20)
            food.y = random.randrange(0, 600, 20)
            eatSong.play(0)
    def game():
        global state
        if state == 1:
            screen.fill([0, 0, 0])
            pygame.draw.rect(screen,[255, 255, 255],(0, 0, 600, 600), 3)
            snake.draw()
            snake.step()
            food.draw()
            checkHit()
            outCanvas()
            writeScore()
            # touchBody()
        else :
            myFont= pygame.font.SysFont('simhei', 100)
            s = myFont.render('Game Over!', True , [0,255,255])
            screen.blit(s, (50,200))
            bgSong.fadeout(5000)

    def writeScore():
        global score
        myFont = pygame.font.SysFont('simhei', 20)
        s = myFont.render('Score :' + str(score), True, [0, 0, 255])
        screen.blit(s, (0, 0))

    def outCanvas():
        global state
        head = snake.body[0]
        if head.x >= 600 or head.x <= -20 or head.y >= 600 or head.y <= -20:
            state = 0
            endSong.play(0)
    # def touchBody():
    #     global state
    #     if snake.body[0].x

    food = Food()
    snake = Snake()

    #使用時間間隔來控制迴圈
    lastTime = time.time()

    while True:
        now = time.time()
        if now - lastTime >= 0.2:
            game()
            lastTime = now


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                #通過鍵盤改變蛇的位置
            if event.type == KEYDOWN:
                if   event.key == K_UP:
                    # if snake.direction == 'down':
                    #     break
                    # else:
                        snake.direction = 'top'
                elif event.key == K_DOWN:
                    # if snake.direction == 'top':
                    #     break
                    # else:
                        snake.direction = 'down'
                elif event.key == K_RIGHT:
                    # if snake.direction == 'left':
                    #     break
                    # else:
                        snake.direction = 'right'
                elif event.key == K_LEFT:
                    # if snake.direction == 'right':
                    #     break
                    # else:
                        snake.direction = 'left'
        pygame.display.update()

if __name__ == "__main__" :
    state = 1
    score = 0
    main()