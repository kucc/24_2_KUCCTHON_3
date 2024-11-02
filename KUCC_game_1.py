import pygame
import random

pygame.init()


width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

running = True

background = pygame.image.load("C:/Users/H/Desktop/background.png")
character = pygame.image.load("C:/Users/H/Desktop/rocket.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = width / 2 - character_width / 2
character_y_pos = height - character_height

game_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 100)

total_time = 60

start_ticks = pygame.time.get_ticks()

class Enemy_large:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_rect().size
        self.x_pos = random.randint(0, screen_width - self.width)
        self.y_pos = random.randint(0, screen_height // 2)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = random.uniform(0.7, 1.0)

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

    def move(self):
        self.y_pos += self.speed
        if self.y_pos > self.screen_height:
            self.y_pos = random.randint(-100, -self.height)
            self.x_pos = random.randint(0, self.screen_width - self.width)
            self.speed = random.uniform(0.7, 1.0)

class Enemy_small:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_rect().size
        self.x_pos = random.randint(0, screen_width - self.width)
        self.y_pos = random.randint(0, screen_height // 2)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = random.uniform(1.0, 1.5)

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

    def move(self):
        self.y_pos += self.speed
        if self.y_pos > self.screen_height:
            self.y_pos = random.randint(-100, -self.height)
            self.x_pos = random.randint(0, self.screen_width - self.width)
            self.speed = random.uniform(1.0, 1.5)

character_speed = 0.5

pressed_keys = set()

enemy_count = 5
enemies_large = [Enemy_large("C:/Users/H/Desktop/asteroid_large.png", width, height) for _ in range(enemy_count)]
enemies_small = [Enemy_small("C:/Users/H/Desktop/asteroid.png", width, height) for _ in range(enemy_count)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                pressed_keys.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                pressed_keys.discard(event.key)
        keys = pygame.key.get_pressed()
        to_x = 0
        to_y = 0
        if pygame.K_w in pressed_keys  and not keys[pygame.K_s]:
            to_y = -character_speed
        elif pygame.K_s in pressed_keys and not keys[pygame.K_w]:
            to_y = character_speed
        if pygame.K_a in pressed_keys and not keys[pygame.K_d]:
            to_x = -character_speed
        elif pygame.K_d in pressed_keys and not keys[pygame.K_a]:
            to_x = character_speed
    
    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > width - character_width:
        character_x_pos = width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > height - character_height:
        character_y_pos = height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos



    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    game_over = game_over_font.render("Game Over", True, (255,255,255))
    game_clear = game_over_font.render("Game clear!", True, (255,255,255))
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time <= 0:
        screen.blit(game_clear, (400, 200))
        running = False

    character_rect = pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)
    for enemy in enemies_large:
        enemy.move()
        enemy.draw(screen)
        enemy_rect = pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height)
        if character_rect.colliderect(enemy_rect):
            screen.blit(game_over, (430, 200))
            running = False
    for enemy in enemies_small:
        enemy.move()
        enemy.draw(screen)
        enemy_rect = pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height)
        if character_rect.colliderect(enemy_rect):
            screen.blit(game_over, (430, 200))
            running = False
    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()