import pygame
import random
import time
import math
from pygame import mixer

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((1200, 800))

# 제목 및 아이콘
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/ufo.png') 
pygame.display.set_icon(icon)

# 플레이어
player_img = pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/player.png')  # 플레이어 이미지 파일 필요
player_x = 550
player_y = 700
player_x_change = 0

# 보스
boss_img = pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/boss.png')
boss_x = random.randint(0, 1070)
boss_y = 50
boss_x_change = 0.1


# 적
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 10

#장애물

barrier_img = []
barrier_x = []
barrier_y = []
barrier_x_change = []
num_of_barriers = 6

for i in range(num_of_barriers):
    barrier_img.append(pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/barrier.png')) # 장애물 이미지 바꾸기
    barrier_x.append(200*i)
    
    barrier_y.append(550)
    barrier_x_change.append(0.3)
  

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/enemy.png'))  # 적 이미지 파일 필요
    enemy_x.append(random.randint(0, 1185)) 
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.2)
    enemy_y_change.append(40)

# 총알
bullet_img = pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/bullet.png')  # 총알 이미지 파일 필요
bullet_x = 0
bullet_y = 700
bullet_x_change = 0
bullet_y_change = 0.2
bullet_state = "ready"  # "ready" - 대기 상태, "fire" - 발사 상태

# 보스 총알

bossbullet_img = pygame.image.load('C:/Users/giora/OneDrive/바탕 화면/python/bossbullet.png')  # 총알 이미지 파일 필요
bossbullet_x = 0
bossbullet_y = 50
bossbullet_x_change = 0
bossbullet_y_change = -0.2
bossbullet_state = "ready"  # "ready" - 대기 상태, "fire" - 발사 상태


# 점수
score_value = 0
life_value = 3
font = pygame.font.Font('freesansbold.ttf', 32)
text_score_x = 10
text_score_y = 10
text_life_x = 10
text_life_y = 40

# 게임 종료
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_life(x, y):
    life = font.render("Life : " + str(life_value), True, (255, 255, 255))
    screen.blit(life, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (370, 300))


def game_complete_text():
    over_text = over_font.render("COMPLETE", True, (255, 255, 255))
    screen.blit(over_text, (365, 300))


def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def boss(x, y):
    screen.blit(boss_img, (x, y))

def barrier(x, y, i):
    screen.blit(barrier_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 30, y + 10))

def fire_bossbullet(x, y):
    global bossbullet_state
    bossbullet_state = "fire"
    screen.blit(bossbullet_img, (x + 30, y + 130))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance < 27

def barrier_collision(barrier_x, barrier_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(barrier_x - bullet_x, 2) + math.pow(barrier_y - bullet_y, 2))
    return distance < 27

def boss_collision(boss_x, boss_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(boss_x - bullet_x, 2) + math.pow(boss_y - bullet_y, 2))
    return distance < 127

def player_collision(bossbullet_x, bossbullet_y, player_x, player_y):
    distance = math.sqrt(math.pow(bossbullet_x - player_x, 2) + math.pow(bossbullet_y - player_y, 2))
    return distance < 50

# 게임 루프
running = True
flag = 0
flag_score = random.randint(300,700)
direction =1
while running:
    # 배경 색상 설정
    screen.fill((0, 0, 0))
    flag+=1
    if flag>flag_score:
        direction*=-1
        flag = 0
        flag_score = flag_score = random.randint(500,3000)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키보드 입력 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2

                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    
    
    boss_x += boss_x_change
        

    boss_x_change = direction*0.1
    if boss_x <= 0: 
        boss_x_change = 0.1
    elif boss_x >= 1070:
        boss_x_change = -0.1

    
    # 플레이어 위치 업데이트
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 1186:
        player_x = 1186

    #보스 맞춤
    boss_collided = boss_collision(boss_x, boss_y, bullet_x, bullet_y)

    if boss_collided:
        bullet_y = 700
        bullet_state = 'ready'
        score_value += 1

    #플레이어 맞음
    player_collided = player_collision(bossbullet_x, bossbullet_y, player_x, player_y)

    if player_collided:
        bossbullet_y = 50
        bossbullet_state = 'ready'
        life_value -= 1


    # 장애물 위치 업데이트
     
    for i in range(num_of_barriers):
        barrier_x[i] += barrier_x_change[i]   
        
        if barrier_x[i] >= 1200:
            barrier_x[i] = 0

        barrier_collided = barrier_collision(barrier_x[i], barrier_y[i], bullet_x, bullet_y)

        if barrier_collided:
            bullet_y = 700
            bullet_state = 'ready'

        barrier(barrier_x[i], barrier_y[i], i)

    # 적 위치 업데이트
    for i in range(num_of_enemies):
        # 게임 종료 조건
        if enemy_y[i] > 760:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            for j in range(num_of_barriers):
                barrier_y[j] = 2000
            bullet_y_change = 0
            boss_x_change = 0
            bossbullet_y_change = 0
            game_over_text()
            break


        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 1186:
            enemy_x_change[i] = -0.2
            enemy_y[i] += enemy_y_change[i]

    
            

        # 충돌 확인
        enemy_collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        

        if enemy_collision:
            bullet_y = 700
            bullet_state = "ready"
            enemy_x[i] = random.randint(0, 1135)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

            
    if score_value == 5 : 
        for j in range (num_of_enemies):
            enemy_y[j] = 2000
        for j in range(num_of_barriers):
            barrier_y[j] = 2000
        bullet_y_change = 0
        boss_x_change = 0
        bossbullet_y_change = 0
        game_complete_text()
        break

    if life_value == 0 : 
        for j in range (num_of_enemies):
            enemy_y[j] = 2000
        for j in range(num_of_barriers):
            barrier_y[j] = 2000
        bullet_y_change = 0
        boss_x_change = 0
        bossbullet_y_change = 0
        game_over_text()
        pygame.time.delay(2000)
        break

    if bossbullet_y >= 780:
        bossbullet_y = 50
        bossbullet_state = 'ready'
    if bossbullet_state == 'ready':
        bossbullet_x = boss_x 
        fire_bossbullet(bossbullet_x, bossbullet_y)
    if bossbullet_state == "fire":
        fire_bossbullet(bossbullet_x, bossbullet_y)
        bossbullet_y -= bossbullet_y_change

    # 총알 위치 업데이트
    if bullet_y <= 0:
        bullet_y = 700
        bullet_state = "ready"
    if bullet_state == "ready":
        bullet_x = player_x
        fire_bullet(bullet_x, bullet_y)
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    boss(boss_x, boss_y)
    player(player_x, player_y)
    show_score(text_score_x, text_score_y)
    show_life(text_life_x, text_life_y)
    pygame.display.update()