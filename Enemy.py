import threading
import pygame
import time
import random


class EnemySprite(threading.Thread):

    def __init__(self, gameDisplay, start_lightning):

        threading.Thread.__init__(self)

        self.gameDisplay = gameDisplay

        self.enemy_boss = [pygame.image.load("Ganon Sprites/ganon 1.png"),
                      pygame.image.load("Ganon Sprites/ganon 2.png"),
                      pygame.image.load("Ganon Sprites/ganon 3.png"),
                      pygame.image.load("Ganon Sprites/ganon 4.png"),
                      pygame.image.load("Ganon Sprites/ganon 5.png"),
                      pygame.image.load("Ganon Sprites/ganon 6.png"),
                      pygame.image.load("Ganon Sprites/ganon 7.png"),
                      pygame.image.load("Ganon Sprites/ganon 8.png"),
                      ]

        # resizing the enemy sprite images
        temp_index = 0
        while temp_index < 8:
            self.enemy_boss[temp_index] = pygame.transform.scale(self.enemy_boss[temp_index], (142, 122))
            temp_index += 1

        self.enemy_rect = self.enemy_boss[0].get_rect()
        self.enemy_alive = True
        self.enemy_index = 79
        self.enemy_speed = 2

        self.move_left = False
        self.move_right = False

        # lightning objects
        self.bolt_obj = EnemyLightning(gameDisplay, self.enemy_rect)

        self.start_lightning = start_lightning

    def begin_lightning(self):
        if self.start_lightning:
            self.bolt_obj.start()

    def get_enemy_rect(self):
        return self.enemy_rect

    def move_enemy(self):
        if self.enemy_rect.x >= 658:
            self.move_left = True
            self.move_right = False
        elif self.enemy_rect.x <= 0:
            self.move_left = False
            self.move_right = True

        if self.move_left:
            self.enemy_rect.move_ip(-self.enemy_speed, 0)
        elif self.move_right:
            self.enemy_rect.move_ip(self.enemy_speed, 0)

    def run(self):

        while self.enemy_alive:

            self.move_enemy()
            time.sleep(0.005)

            self.gameDisplay.blit(self.enemy_boss[self.enemy_index//10], self.enemy_rect)
            pygame.display.update(self.enemy_rect)

            self.enemy_index += 1

            if self.enemy_index > 78:
                self.enemy_index = 0


class EnemyFlames(threading.Thread):

    def __init__(self, gameDisplay):

        threading.Thread.__init__(self)

        self.gameDisplay = gameDisplay
        self.flame = [pygame.image.load("Flames/flame_a_0001.png"),
                      pygame.image.load("Flames/flame_a_0002.png"),
                      pygame.image.load("Flames/flame_a_0003.png"),
                      pygame.image.load("Flames/flame_a_0004.png"),
                      pygame.image.load("Flames/flame_a_0005.png"),
                      pygame.image.load("Flames/flame_a_0006.png"),
                      ]

        self.fire_index = 1
        self.fire_speed = 5

        self.fire_rect = self.flame[0].get_rect(center=(random.randint(26, 774), 108))
        self.flame_hit_rect = (self.fire_rect.x,
                               self.fire_rect.y + self.fire_rect.height - 56,
                               50, 56)

        self.run_flame = True

    def run(self):

        while self.run_flame:

            if self.fire_rect.y >= 395:
                self.fire_rect = self.flame[0].get_rect(center=(random.randint(26, 774), 108))

            self.fire_rect.move_ip(0, self.fire_speed)
            time.sleep(0.008)

            self.flame_hit_rect = (self.fire_rect.x + self.fire_rect.width/2 - 25,
                                   self.fire_rect.y + self.fire_rect.height/2 - 28,
                                   50, 56)

            self.gameDisplay.blit(self.flame[self.fire_index], self.fire_rect)
            pygame.display.update(self.fire_rect)

            self.fire_index += 1

            if self.fire_index > 5:
                self.fire_index = 0


class EnemyLightning(threading.Thread):

    def __init__(self, gameDisplay, enemy_rect):

        threading.Thread.__init__(self)

        self.gameDisplay = gameDisplay

        self.bolt_1 = pygame.image.load("Lightning/bolt_strike_0001.png")
        self.bolt_2 = pygame.image.load("Lightning/bolt_strike_0002.png")
        self.bolt_3 = pygame.image.load("Lightning/bolt_strike_0003.png")
        self.bolt_4 = pygame.image.load("Lightning/bolt_strike_0004.png")
        self.bolt_5 = pygame.image.load("Lightning/bolt_strike_0005.png")
        self.bolt_6 = pygame.image.load("Lightning/bolt_strike_0006.png")
        self.bolt_7 = pygame.image.load("Lightning/bolt_strike_0007.png")
        self.bolt_8 = pygame.image.load("Lightning/bolt_strike_0008.png")
        self.bolt_9 = pygame.image.load("Lightning/bolt_strike_0009.png")
        self.bolt_10 = pygame.image.load("Lightning/bolt_strike_0010.png")

        self.bolt_rect = self.bolt_1.get_rect(center=(enemy_rect.x + 48,
                                                      enemy_rect.y + enemy_rect.height+59))
        self.enemy_rect = enemy_rect
        self.run_lightning = True
        self.bolt_attack = False

    def set_enemy_rect(self, enemy_rect):
        self.enemy_rect = enemy_rect

    def bolt_update(self):
        self.bolt_rect = self.bolt_1.get_rect(center=(self.enemy_rect.x + 48,
                                                      self.enemy_rect.y +
                                                      self.enemy_rect.height + 59))

    def run(self):

        while self.run_lightning:

            # lightning does not do damage to the player yet
            self.bolt_attack = False

            # chance for people to attack
            # enemy's lightning attack will not happen for the next 5-10 seconds
            time.sleep(random.randint(5, 10))

            start_time = time.time() + 3

            # warning of the sign of enemy lightning attack
            while time.time() < start_time and self.run_lightning:
                time.sleep(0.1)
                self.bolt_update()
                self.gameDisplay.blit(self.bolt_1, self.bolt_rect)
                pygame.display.update(self.bolt_rect)

            # lightning now does damage to the player
            self.bolt_attack = True

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_2, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_3, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_4, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_5, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_6, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_7, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_8, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_9, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

            self.bolt_update()
            self.gameDisplay.blit(self.bolt_10, self.bolt_rect)
            pygame.display.update(self.bolt_rect)
            time.sleep(0.01)

