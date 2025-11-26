import pygame
import random
import os

FPS = 60
WIDTH = 600
HEIGHT = 700

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINERED = (210, 17, 17)
YELLOW = (255, 255, 0)

# Game initialization and create window
life = 3
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooting")
clock = pygame.time.Clock()

# Load images
background_img = pygame.image.load(
    os.path.join("img", "halloween-background-with-zombies-tombstones-vector-21424986.jpg")).convert()
player_img = pygame.image.load(os.path.join("img", "圖片 3.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img)
bullet_img = pygame.image.load(os.path.join("img", "圖片 1.png")).convert()
zombie1_img = pygame.image.load(os.path.join("img", "brownzombie.png")).convert()
zombie2_img = pygame.image.load(os.path.join("img", "yellowzombie.png")).convert()
zombie3_img = pygame.image.load(os.path.join("img", "redzombie.png")).convert()
life_imgs = []
for i in range(4):
    life_img = pygame.image.load(os.path.join("img", f"life-{i + 1}.png")).convert()
    life_img.set_colorkey(WHITE)
    life_imgs.append(pygame.transform.scale(life_img, (120, 40)))
# Load music and sound effects
shoot_sound = pygame.mixer.Sound(os.path.join("sound", "GunShotSnglShotIn PE1097906.mp3"))
die_sound1 = pygame.mixer.Sound(os.path.join("sound", "die-short.mp3"))
up_sound = pygame.mixer.Sound(os.path.join("sound", "1up.mp3"))
pygame.mixer.music.load(os.path.join("sound", "60_Second-2021-05-07_-_Imminent_Threat_-_www.FesliyanStudios.com_.mp3"))
pygame.mixer.music.set_volume(0.4)

font_name = os.path.join("Butcherman-Regular.ttf")


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WINERED)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def draw_HighestScore(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_zombie():
    z = Zombie()
    all_sprites.add(z)
    zombies.add(z)


def new_zombie2():
    z = Zombie2()
    all_sprites.add(z)
    zombies2.add(z)


def new_zombie3():
    z = Zombie3()
    all_sprites.add(z)
    zombies3.add(z)


def draw_init():
    screen.blit(background_img, (0, 0))
    draw_text(screen, 'ZOMBIE SHOOTING', 61, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, 'Arrows~ move the weapon', 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Space~ shoot', 22, WIDTH / 2, HEIGHT / 1.75)
    draw_text(screen, 'press to start!', 22, WIDTH / 2, HEIGHT * 3 / 4)
    draw_text(screen, 'WARNING: Do not shoot the red zombie', 20, WIDTH / 2, HEIGHT * 2 / 3)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # Get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (70, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self):
        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 5000:
            self.gun -= 1
            self.gun_time = now

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        if not (self.hidden):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.gun >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 500)

    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()


class Life(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = life_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 30

    def update(self):
        global life
        if life == 3:
            self.image = life_imgs[0]
        if life == 2:
            self.image = life_imgs[1]
        if life == 1:
            self.image = life_imgs[2]
        if life == 0:
            self.image = life_imgs[3]


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = pygame.transform.scale(zombie1_img, (140, 200))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(100, 400)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top >= HEIGHT:
            global life
            life -= 1
            die_sound1.play()
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 8)
            self.speedx = random.randrange(-3, 3)


class Zombie2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = pygame.transform.scale(zombie2_img, (140, 200))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(100, 400)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top >= HEIGHT:
            global life
            life -= 1
            die_sound1.play()
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


class Zombie3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = pygame.transform.scale(zombie3_img, (140, 200))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(100, 400)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (30, 54))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


pygame.mixer.music.play(-1)

# Game loop
show_init = True
running = True
HighestScore = 0
attack = 0
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        zombies = pygame.sprite.Group()
        zombies2 = pygame.sprite.Group()
        zombies3 = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        new_zombie()
        new_zombie2()
        new_zombie3()
        life_bar = Life()
        all_sprites.add(life_bar)
        score = 0
        life = 3

    clock.tick(FPS)
    # Get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update game
    all_sprites.update()

    # Check collision between zombies and bullets
    hits = pygame.sprite.groupcollide(zombies, bullets, True, True)
    for hit in hits:
        attack += 1
        score += 10 * attack * 1.25
        if score >= HighestScore:
            HighestScore = score
        new_zombie()
    hits2 = pygame.sprite.groupcollide(zombies2, bullets, True, True)
    for hit in hits2:
        attack += 1
        score += 20 * attack * 1.25
        if score >= HighestScore:
            HighestScore = score
        new_zombie2()
    hits3 = pygame.sprite.groupcollide(zombies3, bullets, True, True)
    for hit in hits3:
        attack = 0
        life -= 1
        die_sound1.play()
        if score >= HighestScore:
            HighestScore = score
        new_zombie3()
    hitss = pygame.sprite.spritecollide(player, zombies, True, pygame.sprite.collide_circle)
    for hit in hitss:
        attack = 0
        life -= 1
        die_sound1.play()
        new_zombie()
    hitss2 = pygame.sprite.spritecollide(player, zombies2, True, pygame.sprite.collide_circle)
    for hit in hitss2:
        attack = 0
        life -= 1
        die_sound1.play()
        new_zombie2()
    hitss3 = pygame.sprite.spritecollide(player, zombies3, True, pygame.sprite.collide_circle)
    for hit in hitss3:
        life += 2
        up_sound.play()
        if life >= 3:
            life = 3
        new_zombie3()
    if life == 0:
        show_init = True

    # Screen display
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 5)
    draw_HighestScore(screen, 'Highest Score' + ' ' + str(HighestScore), 18, WIDTH / 5, 15)
    draw_text(screen, str(attack) + ' Combo(s)', 25, WIDTH / 2, 20)
    pygame.display.update()

pygame.quit()