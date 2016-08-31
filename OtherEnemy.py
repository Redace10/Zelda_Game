import pygame
import threading
import time


class NarutoEnemy(threading.Thread):

    naruto_front = [pygame.image.load("Naruto/Naruto Front/naruto front 1.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 2.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 3.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 4.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 5.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 6.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 7.png"),
                    pygame.image.load("Naruto/Naruto Front/naruto front 8.png")
                    ]
    naruto_back = [pygame.image.load("Naruto/Naruto Back/naruto back 1.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 2.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 3.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 4.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 5.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 6.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 7.png"),
                   pygame.image.load("Naruto/Naruto Back/naruto back 8.png")
                   ]

    poison_tree_1 = (0, 397, 55, 70)
    poison_tree_2 = (375, 290, 55, 70)
    poison_tree_3 = (162, 65, 55, 70)
    poison_tree_4 = (550, 129, 55, 70)

    def __init__(self, gameDisplay, zelda_map):

        threading.Thread.__init__(self)
        self.naruto_alive = True
        self.naruto_index = 0
        self.naruto_rect = self.naruto_front[self.naruto_index].get_rect(center=(100, 98))
        self.gameDisplay = gameDisplay
        self.naruto_speed = 2
        self.move_Up = False
        self.move_Down = False
        self.zelda_map = zelda_map
        self.temp_naruto_rect = self.naruto_rect

    def move_Naruto(self):
        if self.naruto_rect.y >= 330:
            self.move_Up = True
            self.move_Down = False
        elif self.naruto_rect.y <= 72:
            self.move_Up = False
            self.move_Down = True

        if self.move_Up:
            self.naruto_rect.move_ip(0, -self.naruto_speed)
        elif self.move_Down:
            self.naruto_rect.move_ip(0, self.naruto_speed)

    def run(self):

        while self.naruto_alive:

            self.move_Naruto()
            time.sleep(0.008)

            temp_center_x = self.naruto_rect.x + self.naruto_rect.width/2
            temp_center_y = self.naruto_rect.y + self.naruto_rect.height/2

            if self.move_Down:
                temp_width = self.naruto_front[self.naruto_index//10].get_width()
                temp_height = self.naruto_front[self.naruto_index//10].get_height()
            elif self.move_Up:
                temp_width = self.naruto_back[self.naruto_index // 10].get_width()
                temp_height = self.naruto_back[self.naruto_index // 10].get_height()

            self.temp_naruto_rect = (temp_center_x - temp_width/2,
                                     temp_center_y - temp_height/2,
                                     temp_width, temp_height)

            if self.move_Down:
                self.gameDisplay.blit(self.naruto_front[self.naruto_index//10], self.naruto_rect)
            elif self.move_Up:
                self.gameDisplay.blit(self.naruto_back[self.naruto_index // 10], self.naruto_rect)

            pygame.display.update(self.temp_naruto_rect)

            self.naruto_index += 1

            if self.naruto_index > 79:
                self.naruto_index = 0


class SasukeEnemy(threading.Thread):

    sasuke_front = [pygame.image.load("Sasuke/Sasuke Front/sasuke front 1.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 2.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 3.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 4.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 5.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 6.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 7.png"),
                    pygame.image.load("Sasuke/Sasuke Front/sasuke front 8.png"),
                    ]

    sasuke_back = [pygame.image.load("Sasuke/Sasuke Back/sasuke back 1.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 2.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 3.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 4.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 5.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 6.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 7.png"),
                   pygame.image.load("Sasuke/Sasuke Back/sasuke back 8.png"),
                   ]

    def __init__(self, gameDisplay, zelda_map):
        threading.Thread.__init__(self)
        self.sasuke_alive = True
        self.sasuke_index = 0
        self.sasuke_rect = self.sasuke_front[self.sasuke_index].get_rect(center=(700, 98))
        self.gameDisplay = gameDisplay
        self.sasuke_speed = 3
        self.move_Up = False
        self.move_Down = False
        self.zelda_map = zelda_map
        self.temp_sasuke_rect = self.sasuke_rect

    def move_Sasuke(self):
        if self.sasuke_rect.y >= 330:
            self.move_Up = True
            self.move_Down = False
        elif self.sasuke_rect.y <= 73:
            self.move_Up = False
            self.move_Down = True

        if self.move_Up:
            self.sasuke_rect.move_ip(0, -self.sasuke_speed)
        elif self.move_Down:
            self.sasuke_rect.move_ip(0, self.sasuke_speed)

    def run(self):

        while self.sasuke_alive:

            self.move_Sasuke()
            time.sleep(0.008)

            temp_center_x = self.sasuke_rect.x + self.sasuke_rect.width / 2
            temp_center_y = self.sasuke_rect.y + self.sasuke_rect.height / 2

            if self.move_Down:
                temp_width = self.sasuke_front[self.sasuke_index // 10].get_width()
                temp_height = self.sasuke_front[self.sasuke_index // 10].get_height()
            elif self.move_Up:
                temp_width = self.sasuke_back[self.sasuke_index // 10].get_width()
                temp_height = self.sasuke_back[self.sasuke_index // 10].get_height()

            self.temp_sasuke_rect = (temp_center_x - temp_width/2,
                                     temp_center_y - temp_height/2,
                                     temp_width, temp_height)

            if self.move_Down:
                self.gameDisplay.blit(self.sasuke_front[self.sasuke_index // 10], self.sasuke_rect)
            elif self.move_Up:
                self.gameDisplay.blit(self.sasuke_back[self.sasuke_index // 10], self.sasuke_rect)

            pygame.display.update(self.temp_sasuke_rect)

            self.sasuke_index += 1

            if self.sasuke_index > 79:
                self.sasuke_index = 0


class KakashiEnemy(threading.Thread):
    
    kakashi_sprite = [pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 1.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 2.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 3.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 4.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 5.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 6.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 7.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 8.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 9.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 10.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 11.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 12.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 13.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 14.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 15.png"),
                      pygame.image.load("Kakashi/Kakashi Appear/kakashi appear 16.png"),
                      # index 15

                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 1.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 2.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 3.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 4.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 5.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 6.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 7.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 8.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 9.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 10.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 11.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 12.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 13.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 14.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 15.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 16.png"),
                      pygame.image.load("Kakashi/Kakashi Jutsu/kakashi jutsu 17.png"),
                      # index 32

                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 1.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 2.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 3.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 4.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 5.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 6.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 7.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 8.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 9.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 10.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 11.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 12.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 13.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 14.png"),
                      pygame.image.load("Kakashi/Kakashi Ready/kakashi ready 15.png"),
                      # index 47

                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 1.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 2.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 3.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 4.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 5.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 6.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 7.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 8.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 9.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 10.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 11.png"),
                      pygame.image.load("Kakashi/Kakashi Run/kakashi right 12.png"),
                      # index 59

                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 1.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 2.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 3.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 4.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 5.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 6.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 7.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 8.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 9.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 10.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 11.png"),
                      pygame.image.load("Kakashi/Kakashi Hit/kakashi hit 12.png")
                      #index 71
                      ]

    def __init__(self, gameDisplay, zelda_map):
        threading.Thread.__init__(self)
        self.kakashi_alive = True
        self.kakashi_index = 0
        self.kakashi_rect = self.kakashi_sprite[self.kakashi_index].get_rect(center=(60, 425))
        self.gameDisplay = gameDisplay
        self.kakashi_speed = 10
        self.kakashi_attack_speed = 1
        self.zelda_map = zelda_map
        self.temp_kakashi_rect = (self.kakashi_rect.x, self.kakashi_rect.y, 47, 64)
        self.damage_allowed = True

    def move_Kakashi(self):

        if self.kakashi_index > 600:
            self.kakashi_rect.move_ip(self.kakashi_attack_speed, 0)
        elif self.kakashi_index > 500:
            self.kakashi_rect.move_ip(self.kakashi_speed, 0)
        elif self.kakashi_index == 0:
            self.kakashi_rect.move_ip(-self.kakashi_rect.x + 60, 0)

    def run(self):

        while self.kakashi_alive:

            self.move_Kakashi()

            time.sleep(0.01)

            # boolean for when kakashi does damage
            self.damage_allowed = False
            if self.kakashi_index > 590:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 13, self.kakashi_rect.y + 4, 77, 60)
                self.damage_allowed = True

            # only time when kakashi will damage link
            elif self.kakashi_index > 470:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 6, self.kakashi_rect.y + 13, 85, 54)
                self.damage_allowed = True

            # rect when kakashi is wide open to damage
            elif self.kakashi_index > 320:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 6, self.kakashi_rect.y + 22, 55, 43)
            elif self.kakashi_index > 300:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 7, self.kakashi_rect.y + 14, 54, 51)
            elif self.kakashi_index > 150:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 10, self.kakashi_rect.y + 5, 47, 60)
            elif self.kakashi_index > 60:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 7, self.kakashi_rect.y + 4, 47, 61)
            elif self.kakashi_index > 10:
                self.temp_kakashi_rect = (self.kakashi_rect.x + 6, self.kakashi_rect.y + 12, 56, 53)
            elif self.kakashi_index >= 0:
                self.temp_kakashi_rect = (self.kakashi_rect.x, self.kakashi_rect.y, 57, 64)

            self.gameDisplay.blit(self.kakashi_sprite[self.kakashi_index//10], self.kakashi_rect)

            pygame.display.update(self.kakashi_rect)

            self.kakashi_index += 2

            if self.kakashi_index > 719:
                self.kakashi_index = 0


class LuffyEnenmy(threading.Thread):

    luffy_right = [pygame.image.load("Luffy/Luffy Right/luffy right 1.png"),
                   pygame.image.load("Luffy/Luffy Right/luffy right 2.png"),
                   pygame.image.load("Luffy/Luffy Right/luffy right 3.png"),
                   pygame.image.load("Luffy/Luffy Right/luffy right 4.png"),
                   pygame.image.load("Luffy/Luffy Right/luffy right 5.png"),
                   pygame.image.load("Luffy/Luffy Right/luffy right 6.png"),
                   ]


    luffy_left = [pygame.image.load("Luffy/Luffy Left/luffy left 1.png"),
                  pygame.image.load("Luffy/Luffy Left/luffy left 2.png"),
                  pygame.image.load("Luffy/Luffy Left/luffy left 3.png"),
                  pygame.image.load("Luffy/Luffy Left/luffy left 4.png"),
                  pygame.image.load("Luffy/Luffy Left/luffy left 5.png"),
                  pygame.image.load("Luffy/Luffy Left/luffy left 6.png"),
                  ]

    poison_tree_new_1 = (218, 290, 55, 70)
    poison_tree_new_2 = (310, 108, 55, 70)
    poison_tree_new_3 = (537, 193, 55, 70)
    poison_tree_new_4 = (515, 430, 55, 70)

    def __init__(self, gameDisplay, zelda_map):

        threading.Thread.__init__(self)
        self.luffy_alive = True
        self.luffy_index = 0
        self.luffy_rect = self.luffy_right[self.luffy_index].get_rect(center=(95, 450))
        self.gameDisplay = gameDisplay
        self.luffy_speed = 2
        self.move_Left = False
        self.move_Right = False
        self.zelda_map = zelda_map
        self.temp_luffy_rect = self.luffy_rect

    def move_Luffy(self):
        if self.luffy_rect.x >= 465:
            self.move_Left = True
            self.move_Right = False
        elif self.luffy_rect.x <= 70:
            self.move_Left = False
            self.move_Right = True

        if self.move_Left:
            self.luffy_rect.move_ip(-self.luffy_speed, 0)
        elif self.move_Right:
            self.luffy_rect.move_ip(self.luffy_speed, 0)

    def run(self):

        while self.luffy_alive:

            self.move_Luffy()
            time.sleep(0.008)

            temp_center_x = self.luffy_rect.x + self.luffy_rect.width / 2
            temp_center_y = self.luffy_rect.y + self.luffy_rect.height / 2

            if self.move_Right:
                temp_width = self.luffy_right[self.luffy_index // 10].get_width()
                temp_height = self.luffy_right[self.luffy_index // 10].get_height()
            elif self.move_Left:
                temp_width = self.luffy_left[self.luffy_index // 10].get_width()
                temp_height = self.luffy_left[self.luffy_index // 10].get_height()

            self.temp_luffy_rect = (temp_center_x - temp_width/2, temp_center_y - temp_height/2, temp_width, temp_height)

            if self.move_Right:
                self.gameDisplay.blit(self.luffy_right[self.luffy_index // 10], self.luffy_rect)
            elif self.move_Left:
                self.gameDisplay.blit(self.luffy_left[self.luffy_index // 10], self.luffy_rect)

            pygame.display.update(self.temp_luffy_rect)

            self.luffy_index += 1

            if self.luffy_index > 59:
                self.luffy_index = 0


class PikachuEnenmy(threading.Thread):

    pikachu_right = [pygame.image.load("Pikachu/Pikachu Right/pikachu right 1.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 2.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 3.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 4.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 5.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 6.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 7.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 8.png"),
                     pygame.image.load("Pikachu/Pikachu Right/pikachu right 9.png"),
                     ]


    pikachu_left = [pygame.image.load("Pikachu/Pikachu Left/pikachu left 1.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 2.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 3.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 4.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 5.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 6.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 7.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 8.png"),
                    pygame.image.load("Pikachu/Pikachu Left/pikachu left 9.png"),
                    ]

    def __init__(self, gameDisplay, zelda_map):

        threading.Thread.__init__(self)
        self.pikachu_alive = True
        self.pikachu_index = 0
        self.pikachu_rect = self.pikachu_left[self.pikachu_index].get_rect(center=(708, 330))
        self.gameDisplay = gameDisplay
        self.pikachu_speed = 4
        self.move_Left = False
        self.move_Right = False
        self.zelda_map = zelda_map
        self.temp_pikachu_rect = self.pikachu_rect

    def move_Pikachu(self):
        if self.pikachu_rect.x >= 680:
            self.move_Left = True
            self.move_Right = False
        elif self.pikachu_rect.x <= 282:
            self.move_Left = False
            self.move_Right = True

        if self.move_Left:
            self.pikachu_rect.move_ip(-self.pikachu_speed, 0)
        elif self.move_Right:
            self.pikachu_rect.move_ip(self.pikachu_speed, 0)

    def run(self):

        while self.pikachu_alive:

            self.move_Pikachu()
            time.sleep(0.008)

            temp_center_x = self.pikachu_rect.x + self.pikachu_rect.width / 2
            temp_center_y = self.pikachu_rect.y + self.pikachu_rect.height / 2

            if self.move_Right:
                temp_width = self.pikachu_right[self.pikachu_index // 10].get_width()
                temp_height = self.pikachu_right[self.pikachu_index // 10].get_height()
            elif self.move_Left:
                temp_width = self.pikachu_left[self.pikachu_index // 10].get_width()
                temp_height = self.pikachu_left[self.pikachu_index // 10].get_height()

            self.temp_pikachu_rect = (temp_center_x - temp_width/2, temp_center_y - temp_height/2, temp_width, temp_height)

            if self.move_Right:
                self.gameDisplay.blit(self.pikachu_right[self.pikachu_index // 10], self.pikachu_rect)
            elif self.move_Left:
                self.gameDisplay.blit(self.pikachu_left[self.pikachu_index // 10], self.pikachu_rect)

            pygame.display.update(self.temp_pikachu_rect)

            self.pikachu_index += 1

            if self.pikachu_index > 89:
                self.pikachu_index = 0


class GokuEnenmy(threading.Thread):

    goku_right = [pygame.image.load("Goku/Goku Right/goku right 1.png"),
                  pygame.image.load("Goku/Goku Right/goku right 2.png"),
                  pygame.image.load("Goku/Goku Right/goku right 3.png"),
                  pygame.image.load("Goku/Goku Right/goku right 4.png"),
                  pygame.image.load("Goku/Goku Right/goku right 5.png"),
                  pygame.image.load("Goku/Goku Right/goku right 6.png"),
                  pygame.image.load("Goku/Goku Right/goku right 7.png"),
                  pygame.image.load("Goku/Goku Right/goku right 8.png"),
                  pygame.image.load("Goku/Goku Right/goku right 9.png"),
                  pygame.image.load("Goku/Goku Right/goku right 10.png"),
                  ]


    goku_left = [pygame.image.load("Goku/Goku Left/goku left 1.png"),
                 pygame.image.load("Goku/Goku Left/goku left 2.png"),
                 pygame.image.load("Goku/Goku Left/goku left 3.png"),
                 pygame.image.load("Goku/Goku Left/goku left 4.png"),
                 pygame.image.load("Goku/Goku Left/goku left 5.png"),
                 pygame.image.load("Goku/Goku Left/goku left 6.png"),
                 pygame.image.load("Goku/Goku Left/goku left 7.png"),
                 pygame.image.load("Goku/Goku Left/goku left 8.png"),
                 pygame.image.load("Goku/Goku Left/goku left 9.png"),
                 pygame.image.load("Goku/Goku Left/goku left 10.png"),
                 ]

    def __init__(self, gameDisplay, zelda_map):

        threading.Thread.__init__(self)
        self.goku_alive = True
        self.goku_index = 0
        self.goku_rect = self.goku_right[self.goku_index].get_rect(center=(100, 230))
        self.gameDisplay = gameDisplay
        self.goku_speed = 3
        self.move_Left = False
        self.move_Right = False
        self.zelda_map = zelda_map
        self.temp_goku_rect = self.goku_rect

    def move_Goku(self):
        if self.goku_rect.x >= 470:
            self.move_Left = True
            self.move_Right = False
        elif self.goku_rect.x <= 85:
            self.move_Left = False
            self.move_Right = True

        if self.move_Left:
            self.goku_rect.move_ip(-self.goku_speed, 0)
        elif self.move_Right:
            self.goku_rect.move_ip(self.goku_speed, 0)

    def run(self):

        while self.goku_alive:

            self.move_Goku()
            time.sleep(0.008)

            temp_center_x = self.goku_rect.x + self.goku_rect.width / 2
            temp_center_y = self.goku_rect.y + self.goku_rect.height / 2

            if self.move_Right:
                temp_width = self.goku_right[self.goku_index // 10].get_width()
                temp_height = self.goku_right[self.goku_index // 10].get_height()
            elif self.move_Left:
                temp_width = self.goku_left[self.goku_index // 10].get_width()
                temp_height = self.goku_left[self.goku_index // 10].get_height()

            self.temp_goku_rect = (temp_center_x - temp_width/2, temp_center_y - temp_height/2, temp_width, temp_height)

            if self.move_Right:
                self.gameDisplay.blit(self.goku_right[self.goku_index // 10], self.goku_rect)
            elif self.move_Left:
                self.gameDisplay.blit(self.goku_left[self.goku_index // 10], self.goku_rect)

            pygame.display.update(self.temp_goku_rect)

            self.goku_index += 1

            if self.goku_index > 99:
                self.goku_index = 0