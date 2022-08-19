import pygame
import random

pygame.init()


pygame.init()
size = [500, 500]
win = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
s1 = pygame.mixer.Sound(r"media\122.mp3")
s2 = pygame.mixer.Sound(r"media\211.mp3")
s0 = pygame.mixer.Sound(r"media\del.mp3")


class Game:
    margin = 5
    height = width = 40

    class Dishes():
        margin = 5
        height = width = 40

        def __init__(self, snk):
            self.foodsizex = 40
            self.foodsizey = 40
            self.flagfood = False
            self.snk = snk
            self.colorfood = pygame.Color(70, 25, 100)
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 8)
            self.x11 = 22 + 40 * self.x + (self.x + 1) * 5
            self.x22 = 80 + 40 * self.y + (self.y + 1) * 5
            pygame.draw.rect(win, self.colorfood, (self.x11, self.x22, self.foodsizex, self.foodsizey))

        def RandFoodEqDish(self, snakebody):  # реализовать проверку на рандом еды
            for i in range(len(snakebody)):
                if ((snakebody[i][0] == self.x) and (snakebody[i][1] == self.y)):
                    return False
            return True

        def RandFood(self):
            # self.flagfood=bl
            height = width = 40
            margin = 5
            if (self.flagfood == True):
                while (self.RandFoodEqDish(self.snk) == False):
                    self.x = random.randint(0, 9)
                    self.y = random.randint(0, 8)
                k = random.randint(1, 5)
                if (k == 1):
                    self.colorfood = pygame.Color(255, 0, 0)
                elif (k == 2):
                    self.colorfood = pygame.Color(220, 25, 110)
                elif (k == 3):
                    self.colorfood = pygame.Color(165, 42, 42)
                elif (k == 4):
                    self.colorfood = pygame.Color(0, 0, 255)
                elif (k == 5):
                    self.color = pygame.Color(20, 44, 255)
                self.x11 = 22 + width * self.x + (self.x + 1) * margin
                self.x22 = 80 + height * self.y + (self.y + 1) * margin
                self.flagfood = False
                Game.Snake.coorddishes = [self.x, self.y]
            pygame.draw.rect(win, self.colorfood, (self.x11, self.x22, self.foodsizex, self.foodsizey))

    class Snake():
        margin = 5
        height = width = 40

        def __init__(self):
            self.color = pygame.Color(0, 0, 0)
            # Начальные координаты змейки
            self.snakebody = [[2, 5], [3, 5]]
            self.action = 1
            self.score = 0
            self.fd = Game.Dishes(self.snakebody)
            self.fd.snk = self.snakebody
            self.x = 0
            self.y = 0
            # self.coorddishes=[-10,-10]
            # Голова последняя
            for i in range(2):
                self.x1 = 22 + 40 * self.snakebody[i][0] + (self.snakebody[i][0] + 1) * 5
                self.y1 = 80 + 40 * self.snakebody[i][1] + (self.snakebody[i][1] + 1) * 5
                pygame.draw.rect(win, self.color, (self.x1, self.y1, 40, 40))

        def BoolAddBlock(self):
            if (self.snakebody[len(self.snakebody) - 1][0] == self.fd.x) and (
                    self.snakebody[len(self.snakebody) - 1][1] == self.fd.y):
                pygame.draw.rect(win, (0, 255, 100), (self.x1, self.y1, 40, 40))
                return True
            else:
                return False

        def Bump(self):  # реализовать проверку на рандом еды
            for i in range(len(self.snakebody) - 1):
                if ((self.snakebody[i][0] == self.snakebody[len(self.snakebody) - 1][0]) and (
                        self.snakebody[i][1] == self.snakebody[len(self.snakebody) - 1][1])):
                    return False
            return True

        def ActionSnake(self):
            self.k = pygame.key.get_pressed()
            if ((self.x > 9) or (self.x < 0) or (self.y >= 9) or (self.y < 0) or (self.Bump() == False)):
                Game.flaggame = 2
                s2.play()
                pygame.time.delay(200)
            else:

                if ((self.k[pygame.K_LEFT] == False) and (self.k[pygame.K_RIGHT] == False) and (
                        self.k[pygame.K_UP] == False) and (self.k[pygame.K_DOWN] == False)):
                    if (self.action == 0):
                        self.x = self.snakebody[len(self.snakebody) - 1][0] - 1
                        self.y = self.snakebody[len(self.snakebody) - 1][1]
                        pygame.time.delay(300)
                    elif (self.action == 1):
                        self.x = self.snakebody[len(self.snakebody) - 1][0] + 1
                        self.y = self.snakebody[len(self.snakebody) - 1][1]
                        pygame.time.delay(300)
                    elif (self.action == 2):
                        self.x = self.snakebody[len(self.snakebody) - 1][0]
                        self.y = self.snakebody[len(self.snakebody) - 1][1] - 1
                        pygame.time.delay(300)
                    elif (self.action == 3):
                        self.x = self.snakebody[len(self.snakebody) - 1][0]
                        self.y = self.snakebody[len(self.snakebody) - 1][1] + 1
                        pygame.time.delay(300)
                else:
                    if (self.k[pygame.K_LEFT]):
                        self.x = self.snakebody[len(self.snakebody) - 1][0] - 1
                        self.y = self.snakebody[len(self.snakebody) - 1][1]
                        self.action = 0
                        pygame.time.delay(300)
                    if (self.k[pygame.K_RIGHT]):
                        self.x = self.snakebody[len(self.snakebody) - 1][0] + 1
                        self.y = self.snakebody[len(self.snakebody) - 1][1]
                        self.action = 1
                        pygame.time.delay(300)
                    if (self.k[pygame.K_UP]):
                        self.x = self.snakebody[len(self.snakebody) - 1][0]
                        self.y = self.snakebody[len(self.snakebody) - 1][1] - 1
                        self.action = 2
                        pygame.time.delay(300)
                    if (self.k[pygame.K_DOWN]):
                        self.x = self.snakebody[len(self.snakebody) - 1][0]
                        self.y = self.snakebody[len(self.snakebody) - 1][1] + 1
                        self.action = 3
                        pygame.time.delay(300)
                if ((self.x > 9) or (self.x < 0) or (self.y >= 9) or (self.y < 0) or (self.Bump() == False)):
                    Game.flaggame = 2
                    s2.play()
                    pygame.time.delay(500)
                else:
                    self.snakebody.append([self.x, self.y])
                    if (self.BoolAddBlock() == False):
                        del (self.snakebody[0])
                    else:
                        self.fd.flagfood = True
                        self.score = self.score + 1
                        s1.play()
                        # pygame.mixer.music.play(s1)
                    self.fd.snk = self.snakebody
                    for i in range(len(self.snakebody)):
                        self.x1 = 22 + 40 * self.snakebody[i][0] + (self.snakebody[i][0] + 1) * 5
                        self.y1 = 80 + 40 * self.snakebody[i][1] + (self.snakebody[i][1] + 1) * 5
                        pygame.draw.rect(win, self.color, (self.x1, self.y1, 40, 40))

    flaggame = 0

    def __init__(self):
        # self.action=0
        self.score = 0
        self.sn = Game.Snake()

    @classmethod
    def printTex(self, x, y, massage, fontsize=20, typetex='broadway', color=(255, 0, 0)):
        font = pygame.font.SysFont(typetex, fontsize)
        follow = font.render(massage, 1, color)
        win.blit(follow, (x, y))

    def DrawBlock(x, y, row, column, color):
        pygame.draw.rect(win, color, (x, y, row, column))

    class Button():
        def __init__(self, width, height, inactive_color, active_color):
            self.width = width
            self.height = height
            self.inactive_color = inactive_color
            self.active_color = active_color

        def draw_button(self, x, y, massage, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.height):
                if (click[0] == 1):
                    Game.flaggame = 1
                    s1.play()
                    pygame.time.delay(800)
                    return click[0]
                pygame.draw.rect(win, self.active_color, (x, y, self.width, self.height))

            else:
                pygame.draw.rect(win, self.inactive_color, (x, y, self.width, self.height))
            Game.printTex(x + 45, y + 10, massage, 20, 'broadway')

    def Action(self, flaggame):
        #print(flaggame)
        if (flaggame == 0):  # Поле с началом игры
            pygame.draw.rect(win, (30, 200, 200), (0, 0, 500, 500))
            self.printTex(10, 10, "Snake", 60, "broadway")
            im = pygame.image.load(r"media\1212.png")
            win.blit(im, (50, 0))
            butt = Game.Button(160, 40, (0, 100, 200), (120, 70, 250))
            butt.draw_button(12, 90, "Start")
            pygame.display.update()
        elif (flaggame == 1):
            win.fill((20, 100, 100))
            Game.DrawBlock(15, 73, 470, 422, (0, 140, 110))
            margin = 5
            height1 = width1 = 40
            for col in range(10):
                for roww in range(9):
                    x1 = 22 + width1 * col + (col + 1) * margin
                    y1 = 80 + height1 * roww + (roww + 1) * margin
                    Game.DrawBlock(x1, y1, height1, width1, (0, 255, 100))
            self.sn.ActionSnake()
            self.sn.fd.RandFood()
            font = pygame.font.SysFont("broadway", 60)
            follow = font.render("Score:{0}".format(self.sn.score), 1, (255, 255, 255), (20, 100, 100))
            win.blit(follow, (0, 0))
        else:
            pygame.time.delay(200)
            pygame.draw.rect(win, (30, 200, 200), (0, 0, 500, 500))
            im = pygame.image.load(r"media\apple.png")
            win.blit(im, (200, 259))
            self.printTex(28, 30, "Game Over.", 70)
            font = pygame.font.SysFont("broadway", 50)
            follow2 = font.render(" Your score:{0}".format(self.sn.score), 1, (255, 255, 255))
            win.blit(follow2, (50, 110))
            butt = Game.Button(160, 40, (0, 100, 200), (120, 70, 250))
            a = butt.draw_button(160, 185, "Restart")
            pygame.display.update()
            if (a == 1):
                self.score = 0
                self.sn.snakebody = [[2, 5], [3, 5]]
                flaggame = 1
                self.sn = Game.Snake()


flag = True
flaggame = 0
game = Game()
game.Action(flaggame)
s0.play(-1)
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    game.Action(game.flaggame)
    pygame.display.update()