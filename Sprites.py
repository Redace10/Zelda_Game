import pygame
import time
import threading

class Sprite:



    main_character = [(pygame.image.load("Link Sprites/left_sprites/left 1.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 2.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 3.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 4.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 5.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 6.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 7.png"),
                       pygame.image.load("Link Sprites/left_sprites/left 8.png")),

                      (pygame.image.load("Link Sprites/right_sprites/right 1.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 2.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 3.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 4.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 5.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 6.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 7.png"),
                       pygame.image.load("Link Sprites/right_sprites/right 8.png")),

                      (pygame.image.load("Link Sprites/front_sprites/front 1.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 2.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 3.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 4.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 5.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 6.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 7.png"),
                       pygame.image.load("Link Sprites/front_sprites/front 8.png")),

                      (pygame.image.load("Link Sprites/back_sprites/back 1.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 2.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 3.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 4.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 5.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 6.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 7.png"),
                       pygame.image.load("Link Sprites/back_sprites/back 8.png"))
                      ]

    # Game Maps/Events
    house_part1 = pygame.image.load("Link Houses/link house part 1.png")
    house_part2 = pygame.image.load("Link Houses/link house part 2.png")
    house_part3 = pygame.image.load("Link Houses/link house part 3.png")

    outside_house = pygame.image.load("Game Maps/outside house.png")
    cave_door_closed = pygame.image.load("Game Maps/outside cave door closed.png")
    cave_door_open = pygame.image.load("Game Maps/outside cave door open.png")

    cave_sword = pygame.image.load("Inside Cave/inside cave sword.png")
    cave_no_sword = pygame.image.load("Inside Cave/inside cave without sword.png")

    link_gets_sword = pygame.image.load("link gets sword.png")

    fight_map_1 = pygame.image.load("Game Maps/fight map with block.png")
    fight_map_2 = pygame.image.load("Game Maps/fight map no block.png")
    fight_map_again_1 = pygame.image.load("Game Maps/fight map again with gate.png")
    fight_map_again_2 = pygame.image.load("Game Maps/fight map again no gate.png")

    boss_map = pygame.image.load("zelda map.png")
    boss_battle_map = pygame.image.load("Game Maps/boss battle.png")

    # rectangles for the Game Maps/Events
    door_rect = (194, 0, 7, 34)

    outside_house_rect = (790, 230, 20, 252)

    back_outside_house = (0, 230, 15, 252)

    cave_door_outside = (570, 238, 12, 19)

    inside_cave_entrance_door = (396, 478, 9, 39)
    inside_cave_exit_door = (396, 28, 9, 41)

    sword_area_rect = (359, 176, 84, 68)

    to_fight_again = (378, 37, 47, 33)
    back_to_fight = (375, 500, 47, 33)
    to_boss_battle = (360, 55, 55, 56)

    def get_character_orientation(which_image2):
        return which_image2//10


class LinkAttack(threading.Thread):

    attack_front = [pygame.image.load("Link Attacks/attack_front/attack front 1.png"),
                    pygame.image.load("Link Attacks/attack_front/attack front 2.png"),
                    pygame.image.load("Link Attacks/attack_front/attack front 3.png"),
                    pygame.image.load("Link Attacks/attack_front/attack front 4.png"),
                    pygame.image.load("Link Attacks/attack_front/attack front 5.png")
                    ]
    attack_back = [pygame.image.load("Link Attacks/attack_back/attack back 1.png"),
                   pygame.image.load("Link Attacks/attack_back/attack back 2.png"),
                   pygame.image.load("Link Attacks/attack_back/attack back 3.png"),
                   pygame.image.load("Link Attacks/attack_back/attack back 4.png"),
                   pygame.image.load("Link Attacks/attack_back/attack back 5.png")
                   ]
    attack_left = [pygame.image.load("Link Attacks/attack_left/attack left 1.png"),
                   pygame.image.load("Link Attacks/attack_left/attack left 2.png"),
                   pygame.image.load("Link Attacks/attack_left/attack left 3.png"),
                   pygame.image.load("Link Attacks/attack_left/attack left 4.png"),
                   pygame.image.load("Link Attacks/attack_left/attack left 5.png")
                   ]
    attack_right = [pygame.image.load("Link Attacks/attack_right/attack right 1.png"),
                    pygame.image.load("Link Attacks/attack_right/attack right 2.png"),
                    pygame.image.load("Link Attacks/attack_right/attack right 3.png"),
                    pygame.image.load("Link Attacks/attack_right/attack right 4.png"),
                    pygame.image.load("Link Attacks/attack_right/attack right 5.png")
                    ]

    def __init__(self, gameDisplay, zelda_map, img_rect, moveLeft, moveRight, moveUp, moveDown):
        threading.Thread.__init__(self)
        self.gameDisplay = gameDisplay
        self.zelda_map = zelda_map
        self.img_rect = img_rect
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.moveUp = moveUp
        self.moveDown = moveDown

    def run(self):
        index = 0

        if self.moveLeft:

            while index < 5:
                self.gameDisplay.blit(self.zelda_map, (0, 0))
                pic_background = LinkAttack.attack_left[index].get_rect()
                if index > 0:
                    pic_background = LinkAttack.attack_left[index - 1].get_rect()
                pygame.display.update((self.img_rect.right - 52, self.img_rect.top,
                                       pic_background.width, pic_background.height))
                pic_rect = LinkAttack.attack_left[index].get_rect()
                self.gameDisplay.blit(LinkAttack.attack_left[index], (self.img_rect.right - 52, self.img_rect.top))
                pygame.display.update((self.img_rect.right - 52, self.img_rect.top, pic_rect.width, pic_rect.height))
                index += 1

        elif self.moveRight:

            while index < 5:
                self.gameDisplay.blit(self.zelda_map, (0, 0))
                pic_background = LinkAttack.attack_right[index].get_rect()
                if index > 0:
                    pic_background = LinkAttack.attack_right[index - 1].get_rect()
                pygame.display.update((self.img_rect.left, self.img_rect.top,
                                       pic_background.width, pic_background.height))
                pic_rect = LinkAttack.attack_right[index].get_rect()
                self.gameDisplay.blit(LinkAttack.attack_right[index], (self.img_rect.left, self.img_rect.top))
                pygame.display.update((self.img_rect.left, self.img_rect.top, pic_rect.width, pic_rect.height))
                index += 1

        elif self.moveDown:

            while index < 5:
                self.gameDisplay.blit(self.zelda_map, (0, 0))
                pic_background = LinkAttack.attack_front[index].get_rect()
                if index > 0:
                    pic_background = LinkAttack.attack_front[index - 1].get_rect()
                pygame.display.update((self.img_rect.left, self.img_rect.top,
                                       pic_background.width, pic_background.height))
                pic_rect = LinkAttack.attack_front[index].get_rect()
                self.gameDisplay.blit(LinkAttack.attack_front[index], (self.img_rect.left, self.img_rect.top))
                pygame.display.update((self.img_rect.left, self.img_rect.top, pic_rect.width, pic_rect.height))
                index += 1

        elif self.moveUp:

            self.gameDisplay.blit(self.zelda_map, (0, 0))
            self.gameDisplay.blit(LinkAttack.attack_back[0], (self.img_rect.left, self.img_rect.top))
            pygame.display.update((self.img_rect.left, self.img_rect.top, 45, 48))
            self.gameDisplay.blit(self.zelda_map, (0, 0))
            pygame.display.update((self.img_rect.left, self.img_rect.top, 45, 48))
            self.gameDisplay.blit(LinkAttack.attack_back[1], (self.img_rect.left, self.img_rect.top - 15))
            pygame.display.update((self.img_rect.left, self.img_rect.top - 15, 32, 63))
            self.gameDisplay.blit(self.zelda_map, (0, 0))
            pygame.display.update((self.img_rect.left, self.img_rect.top - 15, 32, 63))
            self.gameDisplay.blit(LinkAttack.attack_back[2], (self.img_rect.left, self.img_rect.top - 15))
            pygame.display.update((self.img_rect.left, self.img_rect.top - 15, 32, 68))
            self.gameDisplay.blit(self.zelda_map, (0, 0))
            pygame.display.update((self.img_rect.left, self.img_rect.top - 15, 32, 68))
            self.gameDisplay.blit(LinkAttack.attack_back[3], (self.img_rect.left - 20, self.img_rect.top - 10))
            pygame.display.update((self.img_rect.left - 20, self.img_rect.top - 10, 52, 56))
            self.gameDisplay.blit(self.zelda_map, (0, 0))
            pygame.display.update((self.img_rect.left - 20, self.img_rect.top - 10, 52, 56))
            self.gameDisplay.blit(LinkAttack.attack_back[4], (self.img_rect.left - 25, self.img_rect.top - 2))
            pygame.display.update((self.img_rect.left - 25, self.img_rect.top - 2, 58, 47))


class Smoke(threading.Thread):

    smoke_sprites = [pygame.image.load("Smoke/smoke_puff_0001.png"),
                     pygame.image.load("Smoke/smoke_puff_0002.png"),
                     pygame.image.load("Smoke/smoke_puff_0003.png"),
                     pygame.image.load("Smoke/smoke_puff_0004.png"),
                     pygame.image.load("Smoke/smoke_puff_0005.png"),
                     pygame.image.load("Smoke/smoke_puff_0006.png"),
                     pygame.image.load("Smoke/smoke_puff_0007.png"),
                     pygame.image.load("Smoke/smoke_puff_0008.png"),
                     pygame.image.load("Smoke/smoke_puff_0009.png"),
                     pygame.image.load("Smoke/smoke_puff_0010.png")
                     ]

    def __init__(self, gameDisplay, zelda_map):
        threading.Thread.__init__(self)
        self.gameDisplay = gameDisplay
        self.zelda_map = zelda_map

    def get_smoke_rect(self, smoke_rect):
        self.smoke_rect = smoke_rect

    def run(self):

        for x in Smoke.smoke_sprites:
            self.gameDisplay.blit(x, self.smoke_rect)
            pygame.display.update(self.smoke_rect)
            time.sleep(0.1)
