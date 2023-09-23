import pygame
from datetime import datetime
import time
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(all_sprites, walls)
        self.image = pygame.Surface([w, h])
        self.image.fill('blue')
        self.rect = pygame.Rect(x, y, w, h)


class Doors(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(all_sprites, doors)
        self.image = pygame.Surface([w, h])
        self.image.fill((0, 100, 100))
        self.rect = pygame.Rect(x, y, w, h)


class Map:
    def __init__(self):
        global dies
        self.width = 23
        self.height = 24
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, '*', 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, '*', 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 0, 0, 'r', 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 1, '-', '-', '-', 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 1, 'o', 6, 'b', 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 1, 6, 6, 6, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 0, 0, 'p', 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, '*', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, '*', 0, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def get_map(self):
        return self.map

    def generate(self, screen):
        x, y = 0, 0
        w, h = 30, 30
        for i in self.map:
            for k in i:
                if k == 0 and dies == 0:
                    Dots(x, y, w, h)
                    # print(1)
                if k == 1:
                    Wall(x, y, w, h)
                if k == '*' and dies == 0:
                    Big_dots(x, y, w, h)
                if k == 'p':
                    img = pygame.image.load('pacman.png').subsurface(pygame.Rect(0, 285, 660, 195))
                    # pygame.image.save(img, 'p.png')
                    pacman = Pacman(x, y, w, h, img, 3, 1)
                    # pacman = Pacman(x, y, w, h)
                if k == 'r':
                    red_ghost = Ghost(x, y, w, h)
                if k == 'b':
                    blue_ghost = Ghost(x, y, w, h)
                if k == 'o':
                    orange_ghost = Ghost(x, y, w, h)
                if k == '-':
                    Doors(x, y, w, h // 2)

                x += w
            x = 0
            y += h
        return pacman, red_ghost, blue_ghost, orange_ghost

    def check_pacman(self):
       # if pacman.check_position():
           # print(pacman.rect.x // 30, pacman.rect.y // 30)
        return pacman.rect.x, pacman.rect.y

    def find_path(self, start, target):
        INF = 1000
        x, y = start
        vx, vy = 0, 0
        distance = [[INF] * self.width for _ in range(self.height)]
        distance[y][x] = 0
        prev = [[None] * self.width for _ in range(self.height + 1)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x <= self.width and 0 <= next_y <= self.height and \
                        not self.map[next_y][next_x] in (1, '-') and distance[next_y][next_x] == INF:
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = target
        # print(distance[y][x])
        if distance[y][x] == INF or start == target:
            return start
        while prev[y][x] != start:
            x, y = prev[y][x]
        if x > start[0]:
            vx = 1
        elif x < start[0]:
            vx = -1
        else:
            vx = 0
        if y > start[1]:
            vy = 1
        elif y < start[1]:
            vy = -1
        else:
            vy = 0
        return vx, vy

    def find_path_2(self, start, target):
        INF = 1000
        x, y = start
        vx, vy = 0, 0
        distance = [[INF] * self.width for _ in range(self.height)]
        distance[y][x] = 0
        prev = [[None] * self.width for _ in range(self.height + 1)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x <= self.width and 0 <= next_y <= self.height and distance[next_y][next_x] == INF:
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = target
        # print(distance[y][x])
        if distance[y][x] == INF or start == target:
            return start
        while prev[y][x] != start:
            x, y = prev[y][x]
        if x > start[0]:
            vx = 1
        elif x < start[0]:
            vx = -1
        else:
            vx = 0
        if y > start[1]:
            vy = 1
        elif y < start[1]:
            vy = -1
        else:
            vy = 0
        return vx, vy


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, sheet, columns, rows):
        super().__init__(all_sprites, hero)
        # self.rect = pygame.Rect(x, y, 200, 200)
        # self.image = pygame.image.load('pacman.png')
        # self.image = self.image.subsurface(pygame.Rect((240, 285), self.rect.size))
        # self.image = pygame.transform.scale(self.image, (w - 2, h - 2))
        # self.rect.size = w - 2, h - 2
        global score
        self.vx = 1
        self.vy = 0
        self.speed = 3
        self.score = score
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y
        self.rect.size = 28, 28

# 0 240 465
#

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, 200, 195)
        frame_location1 = (0, 0)
        frame_location2 = (self.rect.w + 40, 0)
        frame_location3 = (self.rect.w * 2 + 62, 0)
        img1 = sheet.subsurface(pygame.Rect(frame_location1, self.rect.size))
        img2 = sheet.subsurface(pygame.Rect(frame_location2, self.rect.size))
        img3 = pygame.image.load('p.png')
        self.frames.append(pygame.transform.scale(img1, (28, 28)))
        self.frames.append(pygame.transform.scale(img2, (28, 28)))
        self.frames.append(pygame.transform.scale(img3, (28, 28)))
        self.frames.append(pygame.transform.scale(img3, (28, 28)))
        self.frames.append(pygame.transform.scale(img2, (28, 28)))
        self.frames.append(pygame.transform.scale(img1, (28, 28)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.x += self.vx * self.speed
        self.rect.y += self.vy * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= self.vx * self.speed
            self.rect.y -= self.vy * self.speed
        if pygame.sprite.spritecollideany(self, doors):
            self.rect.x -= self.vx * self.speed
            self.rect.y -= self.vy * self.speed
        if pygame.sprite.spritecollideany(self, dots):
            self.score += 10
            pygame.sprite.spritecollideany(self, dots).kill()
            # print(self.score)
        if pygame.sprite.spritecollideany(self, big_dots):
            self.score += 50
            pygame.sprite.spritecollideany(self, big_dots).kill()
            # print(self.score)

    def draw_score(self):
        font = pygame.font.Font(None, 80)
        text1 = font.render('SCORE', True, (255, 0, 0))
        text2 = font.render(str(self.score), True, (255, 100, 100))
        text_x1 = text_x2 = width - 220
        text_y1 = height - 450
        text_y2 = height - 380
        screen.blit(text1, (text_x1, text_y1))
        screen.blit(text2, (text_x2, text_y2))

        # global gx, gy
        # old_x, old_y = self.rect.x, self.rect.y
        # self.rect.x = x
        # self.rect.y = y
        # if pygame.sprite.spritecollideany(self, walls):
        #     # if old_x != self.rect.x and old_y != self.rect.y:
        #     self.rect.x = old_x
        #     self.rect.y = old_y
        #     gx = old_x
        #     gy = old_y
        #     # self.rect.y -= 2
        #     # elif old_x != self.rect.x:
        #     #     self.rect.x -= 2
        #     # elif old_y != self.rect.y:
        #     #     self.rect.y -= 2
    def get_score(self):
        return self.score

    def change_vector(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def rotate(self, angle):
        for i in range(len(self.frames)):
            pygame.image.save(self.frames[i], f'p{i}.png')
            self.frames[i] = pygame.transform.rotate(self.frames[i], angle)

    def check_position(self):
        if self.rect.x % 30 == 0 and self.rect.y % 30 == 0:
            return True
        return False

    def coords_pacman(self):
        return self.rect.x, self.rect.y


class Dots(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(dots)
        self.image = pygame.image.load('dots.png')
        self.image = pygame.transform.scale(self.image, (5, 5))
        # self.image.fill('white')
        # pygame.draw.circle(self.image, 'white', (x + w // 2, y + h // 2), 5)
        self.rect = pygame.Rect(x + 12, y + 12, w - 25, h - 25)


class Big_dots(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(big_dots)
        self.image = pygame.image.load('dots.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = pygame.Rect(x + 6, y + 6, w - 10, h - 10)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        global dies
        super().__init__(all_sprites)
        self.rect = pygame.Rect(x, y, 210, 200)
        self.image = pygame.image.load('pacman.png')
        self.image = self.image.subsurface(pygame.Rect((0, 0), self.rect.size))
        self.image = pygame.transform.scale(self.image, (w - 2, h - 2))
        self.rect.size = w - 2, h - 2
        self.speed = 2

    def update(self, vx, vy):
        global dies
        self.rect.x += vx * self.speed
        self.rect.y += vy * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= vx * self.speed
            self.rect.y -= vy * self.speed
            self.rect.x, self.rect.y = self.rect.x - self.rect.x % 30, self.rect.y - \
                                                self.rect.y % 30
        if pygame.sprite.spritecollideany(self, doors):
            self.rect.x -= vx * self.speed
            self.rect.y -= vy * self.speed
        if pygame.sprite.spritecollideany(self, hero):
            dies += 1



pygame.init()
pygame.display.set_caption('Пакман')
size = width, height = 690, 720
screen = pygame.display.set_mode(size)

font1 = pygame.font.SysFont('Showcard Gothic', 100)
font2 = pygame.font.SysFont('Showcard Gothic', 30)
heading_text = font1.render('Pacman', True, 'yellow')
name_text = font2.render("""Please enter your player's name:""", True, 'red')
helper_text = font2.render("""Click 'UP' to start the game""", True, 'green')
text = ''
name = font2.render(text, True, 'red')
# name_text = font2.render('player name: ', True, 'red')
h_text_x = width // 2 - heading_text.get_width() // 2
h_text_y = 50
n_text_x = 80
n_text_y = 300
text_x = 80
text_y = 400
help_text_x = 120
help_text_y = 600
running = True
con = sqlite3.connect("pacman.sqlite")
cur = con.cursor()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                result = cur.execute(f"""SELECT name_player FROM players_score""").fetchall()
                result = list(map(lambda x: x[0], result))
                print(result)
                if text in result:
                    print(1)
                else:
                    cur.execute(f"""INSERT INTO players_score(name_player, score) VALUES('{text}', {0})""").fetchall()
                    con.commit()
                    print(0)
                running = False
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                name = font2.render(text, True, 'blue')
            symbol = pygame.key.name(event.key)
            if len(symbol) == 1:
                if len(text) < 27:
                    text += symbol
                    name = font2.render(text, True, 'blue')
    screen.blit(heading_text, (h_text_x, h_text_y))
    screen.blit(name_text, (n_text_x, n_text_y))
    pygame.draw.line(screen, 'blue', (text_x, text_y + name.get_height() + 5),
                     (width - text_x, text_y + name.get_height() + 5))
    screen.blit(name, (text_x, text_y))
    screen.blit(helper_text, (help_text_x, help_text_y))
    pygame.display.flip()


all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
dots = pygame.sprite.Group()
big_dots = pygame.sprite.Group()
doors = pygame.sprite.Group()
hero = pygame.sprite.Group()
clock = pygame.time.Clock()
dies = 0
score = 0
while dies != 3:
    map = Map()
    f_b = 0
    f_o = 0
    gx, gy = 9 * 30, 14 * 30 + 2
    dx, dy = 0, 0
    angle = 0
    running = True
    pacman, red_ghost, blue_ghost, orange_ghost = map.generate(screen)
    start_time = time.time()
    # print(start_time)
    blue_ghost_target = (0, 0)
    orange_ghost_target = (0, 0)
    while running:
        time_now = time.time()
        prev_dies = dies
        # print(red_ghost.rect.x // 30, red_ghost.rect.y // 30)
        p_x, p_y = map.check_pacman()
        # print(map.find_path((red_ghost.rect.x // 30, red_ghost.rect.y // 30),
        #                                                    (pacman.rect.x // 30, pacman.rect.y // 30)))
        # print(p_x, p_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                dies = 3
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if (30 - p_x % 30) <= 10:
                        pacman.rect.x = p_x + 30 - p_x % 30
                    elif p_x % 30 < 10:
                        pacman.rect.x = p_x - p_x % 30
                    pacman.change_vector(0, -1)
                    pacman.rotate(90 - angle)
                    angle = 90
                    blue_ghost_target = 0, -2
                    orange_ghost_target = -1, 3
                if event.key == pygame.K_DOWN:
                    if (30 - p_x % 30) <= 10:
                        pacman.rect.x = p_x + 30 - p_x % 30
                    elif p_x % 30 < 10:
                        pacman.rect.x = p_x - p_x % 30
                    pacman.change_vector(0, 1)
                    dy = 30
                    pacman.rotate(270 - angle)
                    angle = 270
                    blue_ghost_target = 0, 2
                    orange_ghost_target = -1, -3
                if event.key == pygame.K_LEFT:
                    if (30 - p_y % 30) <= 10:
                        pacman.rect.y = p_y + 30 - p_y % 30
                    elif p_y % 30 < 10:
                        pacman.rect.y = p_y - p_y % 30
                    pacman.change_vector(-1, 0)
                    dx = -30
                    pacman.rotate(180 - angle)
                    angle = 180
                    blue_ghost_target = -2, 0
                    orange_ghost_target = 3, 1
                if event.key == pygame.K_RIGHT:
                    if (30 - p_y % 30) <= 10:
                        pacman.rect.y = p_y + 30 - p_y % 30
                    elif p_y % 30 < 10:
                        pacman.rect.y = p_y - p_y % 30
                    pacman.change_vector(1, 0)
                    dx = 30
                    pacman.rotate(0 - angle)
                    angle = 0
                    blue_ghost_target = 2, 0
                    orange_ghost_target = -3, -1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    dy = 0
                if event.key == pygame.K_DOWN:
                    dy = 0
                if event.key == pygame.K_LEFT:
                    dx = 0
                if event.key == pygame.K_RIGHT:
                    dx = 0
        # clock.tick()
        screen.fill((0, 0, 0))

        all_sprites.draw(screen)
        dots.draw(screen)
        big_dots.draw(screen)

        gx, gy = gx, gy

        clock.tick(30)
        pacman.update()
        pacman.draw_score()
        # print(map.find_path((red_ghost.rect.x // 30, red_ghost.rect.y // 30),
        #                                                    (pacman.rect.x // 30, pacman.rect.y // 30)))
        r_vx, r_vy = map.find_path((red_ghost.rect.x // 30, red_ghost.rect.y // 30),
                                                           (p_x // 30, p_y // 30))
        red_ghost.update(r_vx, r_vy)
        m = map.get_map()
        # print(m[blue_ghost_target[1] // 30][blue_ghost_target[0] // 30])
        if time_now >= start_time + 10:
            if f_b == 0:
                blue_ghost.rect.x, blue_ghost.rect.y = 8 * 30, 9 * 30
                f_b = 1
            if m[blue_ghost_target[1] // 30][blue_ghost_target[0] // 30] == 0:
                b_vx, b_vy = map.find_path((blue_ghost.rect.x // 30, blue_ghost.rect.y // 30),
                                   (p_x + blue_ghost_target[0] // 30, p_y + blue_ghost_target[1] // 30))
            else:
                b_vx, b_vy = map.find_path((blue_ghost.rect.x // 30, blue_ghost.rect.y // 30),
                                           (p_x // 30, p_y // 30))
            blue_ghost.update(b_vx, b_vy)

        if time_now >= start_time + 20:
            if f_o == 0:
                orange_ghost.rect.x, orange_ghost.rect.y = 8 * 30, 9 * 30
                f_o = 1
            if m[orange_ghost_target[1] // 30][orange_ghost_target[0] // 30] == 0:
                o_vx, o_vy = map.find_path((orange_ghost.rect.x // 30, orange_ghost.rect.y // 30),
                                           (p_x + orange_ghost_target[0] // 30, p_y + orange_ghost_target[1] // 30))
            else:
                o_vx, o_vy = map.find_path((orange_ghost.rect.x // 30, orange_ghost.rect.y // 30),
                                           (p_x // 30, p_y // 30))
                orange_ghost.update(o_vx, o_vy)
        if prev_dies != dies:
            score = pacman.get_score()
            for i in all_sprites:
                i.kill()

            break
        pygame.display.flip()

pygame.display.set_caption('Конец игры')
size = width, height = 690, 720
screen = pygame.display.set_mode(size)

result = cur.execute(f"""SELECT score FROM players_score WHERE name_player = '{text}'""").fetchall()
if result[0][0] < score:
    cur.execute(f"""UPDATE players_score SET score = {score} WHERE name_player = '{text}'""").fetchall()
    con.commit()

font = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None, 40)
text_g = font.render('Game Over', True, (255, 0, 0))
text_score = font.render(f'Score: {score}', True, 'yellow')
players = cur.execute(f"""SELECT * FROM players_score""").fetchall()
players.sort(key=lambda x: x[1], reverse=True)
top = players[:5]
t_text = ['Top players:']
for i in range(len(top)):
    t_text.append(f'{i + 1}.{top[i][0]} - {top[i][1]}')
text_top_x = 100
text_top_y = 500
color = 'blue'
for i in t_text:
    if i == 'Top players:':
        color = 'green'
    else:
        color = 'blue'
    text_top = font2.render(i, True, color)
    screen.blit(text_top, (text_top_x, text_top_y))
    text_top_y += text_top.get_height() + 5
text_x_g = width // 2 - text_g.get_width() // 2
text_y_g = height // 2 - text_g.get_height() // 2
text_x_score = width // 2 - text_g.get_width() // 2
text_y_score = 50
screen.blit(text_g, (text_x_g, text_y_g))
screen.blit(text_score, (text_x_score, text_y_score))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

