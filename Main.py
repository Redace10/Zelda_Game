import pygame
import os
import time
from Sprites import Sprite, Smoke, LinkAttack
from Enemy import EnemySprite, EnemyFlames
from Health import Hp
from OtherEnemy import NarutoEnemy, SasukeEnemy, KakashiEnemy, LuffyEnenmy, PikachuEnenmy, GokuEnenmy


# closes threads
def close_threads():
    flame_obj1.run_flame = False
    flame_obj2.run_flame = False
    flame_obj3.run_flame = False
    flame_obj4.run_flame = False
    flame_obj5.run_flame = False

    enemy_obj.bolt_obj.run_lightning = False

    enemy_obj.enemy_alive = False

    close_first_enemy_threads()
    close_second_enemy_threads()


def close_first_enemy_threads():
    naruto_obj.naruto_alive = False
    sasuke_obj.sasuke_alive = False
    kakashi_obj.kakashi_alive = False


def close_second_enemy_threads():
    luffy_obj.luffy_alive = False
    pikachu_obj.pikachu_alive = False
    goku_obj.goku_alive = False


def start_threads():
    flame_obj1.start()
    flame_obj2.start()
    flame_obj3.start()
    flame_obj4.start()
    flame_obj5.start()
    enemy_obj.start_lightning = True
    enemy_obj.start()
    enemy_obj.begin_lightning()


def start_first_enemy_threads():
    naruto_obj.start()
    sasuke_obj.start()
    kakashi_obj.start()


def start_second_enemy_threads():
    luffy_obj.start()
    pikachu_obj.start()
    goku_obj.start()

# centers the game window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# creates Sprite object
sprite_obj = Sprite()

pygame.init()

# plays background song repeatedly
pygame.mixer.music.load("Harp Ballad of the Goddess.mp3")
# pygame.mixer.music.load("The Marching Pirate Spy.mp3")
pygame.mixer.music.play(-1, 0)

x_Display = 800
y_Display = 600

gameDisplay = pygame.display.set_mode((x_Display, y_Display))
game_border = gameDisplay.get_rect()

# threads for the mini enemies
naruto_obj = NarutoEnemy(gameDisplay, sprite_obj.fight_map_2)
sasuke_obj = SasukeEnemy(gameDisplay, sprite_obj.fight_map_2)
kakashi_obj = KakashiEnemy(gameDisplay, sprite_obj.fight_map_2)
luffy_obj = LuffyEnenmy(gameDisplay, sprite_obj.fight_map_2)
pikachu_obj = PikachuEnenmy(gameDisplay, sprite_obj.fight_map_2)
goku_obj = GokuEnenmy(gameDisplay, sprite_obj.fight_map_2)

# threads for the flames
flame_obj1 = EnemyFlames(gameDisplay)
flame_obj2 = EnemyFlames(gameDisplay)
flame_obj3 = EnemyFlames(gameDisplay)
flame_obj4 = EnemyFlames(gameDisplay)
flame_obj5 = EnemyFlames(gameDisplay)

# health objects
health_player = Hp(100, gameDisplay)
health_enemy = Hp(200, gameDisplay)
health_naruto = Hp(200, gameDisplay)
health_sasuke = Hp(200, gameDisplay)
health_kakashi = Hp(200, gameDisplay)
health_luffy = Hp(200, gameDisplay)
health_pikachu = Hp(200, gameDisplay)
health_goku = Hp(200, gameDisplay)

# link's speed
movement_speed = 7

# enemy sprite object
enemy_obj = EnemySprite(gameDisplay, False)


# link's damage toward various enemies
def damage_on_enemies():

    if fight_at_1:
        if main_attack_rect.colliderect(naruto_obj.temp_naruto_rect):
            health_naruto.lose_enemy_health(20)
        elif main_attack_rect.colliderect(sasuke_obj.temp_sasuke_rect):
            health_sasuke.lose_enemy_health(20)
        elif main_attack_rect.colliderect(kakashi_obj.temp_kakashi_rect):
            health_kakashi.lose_enemy_health(15)
    elif fight_at_new_1:
        if main_attack_rect.colliderect(luffy_obj.luffy_rect):
            health_luffy.lose_enemy_health(15)
        elif main_attack_rect.colliderect(pikachu_obj.pikachu_rect):
            health_pikachu.lose_enemy_health(15)
        elif main_attack_rect.colliderect(goku_obj.goku_rect):
            health_goku.lose_enemy_health(10)
    elif fight_at_boss:
        if main_attack_rect.colliderect(enemy_obj.enemy_rect):
            health_enemy.lose_enemy_health(5)


# link loses health when colliding with his enemies
def get_damage():

    if fight_at_1:
        if main_rect.colliderect(naruto_obj.naruto_rect):
            health_player.lose_player_health(2)
        elif main_rect.colliderect(sasuke_obj.sasuke_rect):
            health_player.lose_player_health(1)
        elif main_rect.colliderect(kakashi_obj.temp_kakashi_rect) and kakashi_obj.damage_allowed:
            health_player.lose_player_health(3)
    elif fight_at_new_1:
        if main_rect.colliderect(luffy_obj.luffy_rect):
            health_player.lose_player_health(2)
        elif main_rect.colliderect(pikachu_obj.pikachu_rect):
            health_player.lose_player_health(2)
        elif main_rect.colliderect(goku_obj.goku_rect):
            health_player.lose_player_health(5)

def health_bars_display():

    if fight_at_1:
        health_naruto.health_bars_side_char(health_naruto.health, 535)
        health_sasuke.health_bars_side_char(health_sasuke.health, 558)
        health_kakashi.health_bars_side_char(health_kakashi.health, 581)

        gameDisplay.blit(health_naruto.message_to_screen("Naruto", yellow, 25), [480, 530])
        gameDisplay.blit(health_sasuke.message_to_screen("Sasuke", yellow, 25), [480, 553])
        gameDisplay.blit(health_kakashi.message_to_screen("Kakashi", yellow, 25), [480, 576])

        gameDisplay.blit(health_naruto.message_to_screen("Hp", yellow, 25), [550, 530])
        gameDisplay.blit(health_sasuke.message_to_screen("Hp", yellow, 25), [550, 553])
        gameDisplay.blit(health_kakashi.message_to_screen("Hp", yellow, 25), [550, 576])
    elif fight_at_new_1:
        health_luffy.health_bars_side_char(health_luffy.health, 535)
        health_pikachu.health_bars_side_char(health_pikachu.health, 558)
        health_goku.health_bars_side_char(health_goku.health, 581)

        gameDisplay.blit(health_luffy.message_to_screen("Luffy", yellow, 25), [480, 530])
        gameDisplay.blit(health_pikachu.message_to_screen("Pikachu", yellow, 25), [480, 553])
        gameDisplay.blit(health_goku.message_to_screen("Goku", yellow, 25), [480, 576])

        gameDisplay.blit(health_luffy.message_to_screen("Hp", yellow, 25), [550, 530])
        gameDisplay.blit(health_pikachu.message_to_screen("Hp", yellow, 25), [550, 553])
        gameDisplay.blit(health_goku.message_to_screen("Hp", yellow, 25), [550, 576])
    elif fight_at_boss:
        health_enemy.health_bar_boss(health_enemy.health)
        gameDisplay.blit(health_enemy.message_to_screen("Hp", yellow, 40), [535, 550])

player_dead = False
naruto_dead = False
sasuke_dead = False
kakashi_dead = False
luffy_dead = False
pikachu_dead = False
goku_dead = False
boss_dead = False


# pass in a health object
# smoke explosion when the specific character is dead
def smoke_when_dead():

    # creates Smoke object
    smoke_obj = Smoke(gameDisplay, map)

    global player_dead, naruto_dead, sasuke_dead, kakashi_dead, luffy_dead, pikachu_dead, goku_dead, boss_dead

    if health_player.health <= 0 and not player_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(main_rect.x + main_rect.width / 2, main_rect.y - main_rect.height / 2))
        player_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_naruto.health <= 0 and not naruto_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(naruto_obj.temp_naruto_rect[0] + naruto_obj.temp_naruto_rect[2] / 2,
                    naruto_obj.temp_naruto_rect[1] - naruto_obj.temp_naruto_rect[3] / 2))
        naruto_obj.naruto_alive = False
        naruto_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_sasuke.health <= 0 and not sasuke_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(sasuke_obj.temp_sasuke_rect[0] + sasuke_obj.temp_sasuke_rect[2] / 2,
                    sasuke_obj.temp_sasuke_rect[1] - sasuke_obj.temp_sasuke_rect[3] / 2))
        sasuke_obj.sasuke_alive = False
        sasuke_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_kakashi.health <= 0 and not kakashi_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(kakashi_obj.temp_kakashi_rect[0] + kakashi_obj.temp_kakashi_rect[2] / 2,
                    kakashi_obj.temp_kakashi_rect[1] - kakashi_obj.temp_kakashi_rect[3] / 2))
        kakashi_obj.kakashi_alive = False
        kakashi_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_luffy.health <= 0 and not luffy_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(luffy_obj.temp_luffy_rect[0] + luffy_obj.temp_luffy_rect[2] / 2,
                    luffy_obj.temp_luffy_rect[1] - luffy_obj.temp_luffy_rect[3] / 2))
        luffy_obj.luffy_alive = False
        luffy_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_pikachu.health <= 0 and not pikachu_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(pikachu_obj.temp_pikachu_rect[0] + pikachu_obj.temp_pikachu_rect[2] / 2,
                    pikachu_obj.temp_pikachu_rect[1] - pikachu_obj.temp_pikachu_rect[3] / 2))
        pikachu_obj.pikachu_alive = False
        pikachu_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_goku.health <= 0 and not goku_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(
            center=(goku_obj.temp_goku_rect[0] + goku_obj.temp_goku_rect[2] / 2,
                    goku_obj.temp_goku_rect[1] - goku_obj.temp_goku_rect[3] / 2))
        goku_obj.goku_alive = False
        goku_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()
    elif health_enemy.health <= 0 and not boss_dead:
        smoke_rect = smoke_obj.smoke_sprites[0].get_rect(center=(enemy_obj.enemy_rect.x + 48,
                                                         enemy_obj.enemy_rect.y + enemy_obj.enemy_rect.height / 2))
        boss_dead = True
        smoke_obj.get_smoke_rect(smoke_rect)
        smoke_obj.start()

temp_array = [0, 0, 0, 0, 0, 0]


# rect are moved to other places so that they will not interfere after the characters are dead
def enemies_dead():

    global temp_array

    if naruto_dead and temp_array[0] < 1:
        naruto_obj.naruto_rect.move_ip(1000, 0)
        naruto_obj.temp_naruto_rect = (1000, 0, 100, 100)
        temp_array[0] += 1
    elif sasuke_dead and temp_array[1] < 1:
        sasuke_obj.sasuke_rect.move_ip(1000, 0)
        sasuke_obj.temp_sasuke_rect = (1000, 0, 100, 100)
        temp_array[1] += 1
    elif kakashi_dead and temp_array[2] < 1:
        kakashi_obj.kakashi_rect.move_ip(1000, 0)
        kakashi_obj.temp_kakashi_rect = (1000, 0, 100, 100)
        temp_array[2] += 1
    elif luffy_dead and temp_array[3] < 1:
        luffy_obj.luffy_rect.move_ip(1000, 0)
        luffy_obj.temp_luffy_rect = (1000, 0, 100, 100)
        temp_array[3] += 1
    elif pikachu_dead and temp_array[4] < 1:
        pikachu_obj.pikachu_rect.move_ip(1000, 0)
        pikachu_obj.temp_pikachu_rect = (1000, 0, 100, 100)
        temp_array[4] += 1
    elif goku_dead and temp_array[5] < 1:
        goku_obj.goku_rect.move_ip(1000, 0)
        goku_obj.temp_goku_rect = (1000, 0, 100, 100)
        temp_array[5] += 1

# dimensions where the main character is allowed to move
game_map_restriction_boss_battle = (0, 108, 800, 415)

# orientation of the main character
which_image1 = 0
which_image2 = 0

# orientation of the attacks
left_image2 = 0
right_image2 = 0
front_image2 = 0
back_image2 = 0

# variables for which side the main character is facing
moveUp = moveDown = moveRight = moveLeft = True

# character by default starts at the bottom right of the screen
main_rect = sprite_obj.main_character[0][0].get_rect(center=(784, 500))
main_attack_rect = main_rect

pygame.display.set_caption('Zelda Game')

yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

gameExit = False
gameWin = False
gameLose = False

x_change = 0
y_change = 0

clock = pygame.time.Clock()

quit_button = False

link_has_sword = False

start_of_game = True
starting_threads = True
start_position_home = True

outside_of_house = False
start_position_outside_home = True
start_position_outside_home_back = False

outside_of_cave = False
start_position_outside_cave = True
start_position_outside_cave_back = False
outside_door_open_cave = False

inside_cave_sword_present = False
inside_cave_sword_not_present = False
first_time_inside_cave = True
first_time_link_gets_sword = True

fight_at_1 = False
fight_at_2 = False
first_time_in_fight = True

fight_at_new_1 = False
fight_at_new_2 = False
fight_at_new_3 = False
first_time_in_fight_again = True

fight_at_boss = False

map = sprite_obj.boss_map
# map of current game

# loops until the user clicks the exit button
while not gameExit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or gameWin or gameLose:

            if event.type == pygame.QUIT:
                quit_button = True
            close_threads()
            gameExit = True

        # movement and attack buttons
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
                moveUp = moveDown = moveRight = False
                x_change -= movement_speed
                y_change = 0
                which_image1 = 0

                if left_image2 >= 78:
                    left_image2 = 0
                else:
                    left_image2 += 2

            elif event.key == pygame.K_RIGHT:
                moveRight = True
                moveUp = moveDown = moveLeft = False
                x_change += movement_speed
                y_change = 0
                which_image1 = 1

                if right_image2 >= 78:
                    right_image2 = 0
                else:
                    right_image2 += 2

            elif event.key == pygame.K_DOWN:
                moveDown = True
                moveUp = moveRight = moveLeft = False
                y_change += movement_speed
                x_change = 0
                which_image1 = 2

                if front_image2 >= 78:
                    front_image2 = 0
                else:
                    front_image2 += 2

            elif event.key == pygame.K_UP:
                moveUp = True
                moveDown = moveRight = moveLeft = False
                y_change -= movement_speed
                x_change = 0
                which_image1 = 3

                if back_image2 >= 78:
                    back_image2 = 0
                else:
                    back_image2 += 2

            # attack button
            elif event.key == pygame.K_SPACE and health_player.health > 0 and link_has_sword:
                # pygame.mixer.music.load("Link_Attack_Sound_Effect.mp3")
                # pygame.mixer.music.play(1,0.0)

                attack_obj = LinkAttack(gameDisplay, map, main_rect, moveLeft, moveRight, moveUp, moveDown)
                attack_obj.start()

                if moveLeft:
                    main_attack_rect = pygame.Rect(main_rect.right - 52, main_rect.top, 61, 48)
                elif moveRight:
                    main_attack_rect = pygame.Rect(main_rect.x, main_rect.y, 61, 48)
                elif moveDown:
                    main_attack_rect = pygame.Rect(main_rect.left, main_rect.top, 38, 58)
                elif moveUp:
                    main_attack_rect = pygame.Rect(main_rect.left, main_rect.top - 15, 45, 68)

                damage_on_enemies()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                which_image2 = 0
                left_image2 = right_image2 = 0

            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
                which_image2 = 0
                front_image2 = back_image2 = 0

    if which_image2 >= 78:
        which_image2 = 0
    else:
        if moveUp:
            which_image2 += back_image2
        elif moveDown:
            which_image2 += front_image2
        elif moveLeft:
            which_image2 += left_image2
        elif moveRight:
            which_image2 += right_image2

    if health_player.health > 0:
        main_rect.move_ip(x_change, y_change)

    # beginning of the game
    if start_of_game:

        if start_position_home:

            start_time = time.time() + 3

            while time.time() < start_time:
                gameDisplay.blit(sprite_obj.house_part1, (0, 0))
                pygame.display.update()
            while time.time() < start_time + 3:
                gameDisplay.blit(sprite_obj.house_part2, (0, 0))
                pygame.display.update()
            # position where link wakes up
            main_rect.move_ip(-200, -165)
        start_position_home = False

        gameDisplay.blit(sprite_obj.house_part3, (0, 0))

        # character cannot move outside of the map restrictions
        game_map_restriction_house = (150, 25, 451, 366)
        main_rect.clamp_ip(game_map_restriction_house)

        if main_rect.colliderect(sprite_obj.door_rect) and moveUp:
            start_of_game = False
            outside_of_house = True
            main_rect.move_ip(-300, 0)

    # when link goes outside of his house
    elif outside_of_house:

        map = sprite_obj.outside_house
        # character cannot move outside of the map restrictions
        game_map_restriction_outside_house = (65, 230, 738, 252)
        main_rect.clamp_ip(game_map_restriction_outside_house)

        if start_position_outside_home:
            # moves link to the location of his door
            main_rect.move_ip(72, 0)
        elif start_position_outside_home_back:
            # moves link to the location of where he came from
            main_rect.move_ip(1000, 0)
        start_position_outside_home = False
        start_position_outside_home_back = False

        gameDisplay.blit(sprite_obj.outside_house, (0, 0))

        if main_rect.colliderect(sprite_obj.outside_house_rect) and moveRight:
            outside_of_house = False
            outside_of_cave = True
            start_position_outside_cave = True

    # when link goes to the right of outside his house
    elif outside_of_cave:

        # character cannot move outside of the map restrictions
        game_map_restriction_outside_cave = (0, 230, 736, 252)
        main_rect.clamp_ip(game_map_restriction_outside_cave)

        if start_position_outside_cave:
            # moves link to the location of where he came from
            main_rect.move_ip(-1000, 0)
        elif start_position_outside_cave_back:
            # moves link to the location of the cave entrance
            main_rect.move_ip(-145, -184)

        start_position_outside_cave = False
        start_position_outside_cave_back = False

        if outside_door_open_cave:
            gameDisplay.blit(sprite_obj.cave_door_open, (0, 0))
            map = sprite_obj.cave_door_open
        else:
            gameDisplay.blit(sprite_obj.cave_door_closed, (0, 0))

        if main_rect.colliderect(sprite_obj.back_outside_house) and moveLeft:
            outside_of_house = True
            outside_of_cave = False
            start_position_outside_home_back = True
        elif main_rect.colliderect(sprite_obj.cave_door_outside) and moveUp:
            if not outside_door_open_cave:
                main_rect.move_ip(0, 100)
                outside_door_open_cave = True
            else:
                first_time_inside_cave = True
                outside_of_cave = False
                inside_cave_sword_present = True
                main_rect.move_ip(0, 1000)

    # inside of the turtle cave
    elif inside_cave_sword_present:

        game_map_restriction_inside_cave = (357, 56, 88, 424)
        main_rect.clamp_ip(game_map_restriction_inside_cave)

        if first_time_inside_cave:
            # moves link to the entrance inside the cave
            main_rect.move_ip(-28, 0)
        first_time_inside_cave = False

        if inside_cave_sword_not_present:
            gameDisplay.blit(sprite_obj.cave_no_sword, (0, 0))
            map = sprite_obj.cave_no_sword
        else:
            gameDisplay.blit(sprite_obj.cave_sword, (0, 0))

        if main_rect.colliderect(sprite_obj.inside_cave_entrance_door) and moveDown:
            outside_of_cave = True
            inside_cave_sword_present = False
            start_position_outside_cave_back = True
            main_rect.move_ip(1000, 1000)

        elif main_rect.colliderect(sprite_obj.sword_area_rect) and moveUp and first_time_link_gets_sword:
            inside_cave_sword_not_present = True
            link_has_sword = True

            # when link obtains his sword
            gameDisplay.blit(sprite_obj.cave_no_sword, (0, 0))
            main_rect.move_ip(-main_rect.x, -main_rect.y)
            main_rect.move_ip(383, 166)
            gameDisplay.blit(sprite_obj.link_gets_sword, main_rect)
            pygame.display.update()
            time.sleep(3)
            main_rect.move_ip(5, 40)

            first_time_link_gets_sword = False

        elif main_rect.colliderect(sprite_obj.inside_cave_exit_door) and moveUp:
            inside_cave_sword_present = False
            main_rect.move_ip(1000, 1000)
            fight_at_1 = True
            start_first_enemy_threads()

    elif fight_at_1:

        game_map_restriction_fight_1 = (65, 52, 674, 420)
        main_rect.clamp_ip(game_map_restriction_fight_1)

        if first_time_in_fight:
            # moves link to the entrance outside the cave
            main_rect.move_ip(-325, 0)
        first_time_in_fight = False

        if health_naruto.health <= 0 and health_sasuke.health <= 0 and health_kakashi.health <= 0:
            gameDisplay.blit(sprite_obj.fight_map_2, (0, 0))
            map = sprite_obj.fight_map_2
            fight_at_2 = True
        else:
            gameDisplay.blit(sprite_obj.fight_map_1, (0, 0))
            map = sprite_obj.fight_map_1

        # link loses health when his enemies attack him
        get_damage()

        # link cannot walk through the purple trees
        if (main_rect.colliderect(naruto_obj.poison_tree_1) or
                main_rect.colliderect(naruto_obj.poison_tree_2) or
                main_rect.colliderect(naruto_obj.poison_tree_3) or
                main_rect.colliderect(naruto_obj.poison_tree_4) or
                main_rect.colliderect(naruto_obj.temp_naruto_rect) or
                main_rect.colliderect(sasuke_obj.temp_sasuke_rect) or
                main_rect.colliderect(kakashi_obj.temp_kakashi_rect)):
            # if link gets hit by kakashi's attack
            if main_rect.colliderect(kakashi_obj.temp_kakashi_rect) and kakashi_obj.damage_allowed:
                main_rect.move_ip(100, 0)

            if moveLeft:
                main_rect.move_ip(7, 0)
            elif moveRight:
                main_rect.move_ip(-7, 0)
            elif moveUp:
                main_rect.move_ip(0, 7)
            elif moveDown:

                main_rect.move_ip(0, -7)

            # this if statement is only for naruto and sasuke
            if (main_rect.colliderect(naruto_obj.temp_naruto_rect) or
                    main_rect.colliderect(sasuke_obj.temp_sasuke_rect)):
                if moveLeft:
                    main_rect.move_ip(5, 0)
                if moveRight:
                    main_rect.move_ip(-5, 0)
                if moveUp:
                    main_rect.move_ip(0, 10)
                if moveDown:
                    main_rect.move_ip(0, -10)

        if main_rect.colliderect(sprite_obj.to_fight_again) and moveUp and fight_at_2:
            fight_at_1 = False
            fight_at_new_1 = True
            main_rect.move_ip(0, 1000)
            close_first_enemy_threads()
            start_second_enemy_threads()

    elif fight_at_new_1:

        game_map_restriction_fight_2 = (64, 84, 671, 421)
        main_rect.clamp_ip(game_map_restriction_fight_2)

        if health_luffy.health <= 0 and health_pikachu.health <= 0 and health_goku.health <= 0:
            gameDisplay.blit(sprite_obj.fight_map_again_2, (0, 0))
            map = sprite_obj.fight_map_again_2
            fight_at_new_2 = True
        else:
            gameDisplay.blit(sprite_obj.fight_map_again_1, (0, 0))
            map = sprite_obj.fight_map_again_1

        # link loses health when his enemies attack him
        get_damage()

        # link cannot walk through the purple trees
        if (main_rect.colliderect(luffy_obj.poison_tree_new_1) or
                main_rect.colliderect(luffy_obj.poison_tree_new_2) or
                main_rect.colliderect(luffy_obj.poison_tree_new_3) or
                main_rect.colliderect(luffy_obj.poison_tree_new_4) or
                main_rect.colliderect(luffy_obj.temp_luffy_rect) or
                main_rect.colliderect(pikachu_obj.temp_pikachu_rect) or
                main_rect.colliderect(goku_obj.temp_goku_rect)):
            if moveLeft:
                main_rect.move_ip(7, 0)
            elif moveRight:
                main_rect.move_ip(-7, 0)
            elif moveUp:
                main_rect.move_ip(0, 7)
            elif moveDown:
                main_rect.move_ip(0, -7)

            # this if statement is only for luffy, pikachu, and goku
            if (main_rect.colliderect(luffy_obj.temp_luffy_rect) or
                    main_rect.colliderect(pikachu_obj.temp_pikachu_rect) or
                    main_rect.colliderect(goku_obj.temp_goku_rect)):
                if moveLeft:
                    main_rect.move_ip(12, 0)
                elif moveRight:
                    main_rect.move_ip(-12, 0)
                elif moveUp:
                    main_rect.move_ip(0, 6)
                elif moveDown:
                    main_rect.move_ip(0, -6)

        if main_rect.colliderect(sprite_obj.to_boss_battle) and moveUp and fight_at_new_2:
            fight_at_new_1 = False
            main_rect.move_ip(1000, 1000)
            fight_at_boss = True
            health_player.health = 100

# FIX WHERE THE SMOKE APPEARS

    elif fight_at_boss:

        map = sprite_obj.boss_map
        if starting_threads:
            start_threads()
        starting_threads = False

        if (main_rect.colliderect(flame_obj1.flame_hit_rect) or
                main_rect.colliderect(flame_obj2.flame_hit_rect) or
                main_rect.colliderect(flame_obj3.flame_hit_rect) or
                main_rect.colliderect(flame_obj4.flame_hit_rect) or
                main_rect.colliderect(flame_obj5.flame_hit_rect)):
            if health_player.health > 0:
                main_rect.move_ip(0, 100)
            health_player.lose_player_health(2)

        if main_rect.colliderect(enemy_obj.bolt_obj.bolt_rect) and enemy_obj.bolt_obj.bolt_attack:
            main_rect.move_ip(0, 1000)
            health_player.lose_player_health(30)

        # character cannot move outside of the map restrictions
        main_rect.clamp_ip(game_map_restriction_boss_battle)

        gameDisplay.blit(sprite_obj.boss_map, (0, 0))

    # method that displays the smoke after a character dies
    smoke_when_dead()

    # makes enemies' rectangles useless after they die
    enemies_dead()

    if health_player.health > 0:
        gameDisplay.blit(sprite_obj.main_character[which_image1][Sprite.get_character_orientation(which_image2)],
                         main_rect)
    if health_player.health <= 0:
        gameLose = True

    if health_enemy.health <= 0:
        gameWin = True

    enemy_obj.bolt_obj.set_enemy_rect(enemy_obj.get_enemy_rect())

    gameDisplay.blit(health_player.message_to_screen("Hp", yellow, 40), [40, 550])
    health_player.health_bar_main(health_player.health)
    # displays the enemy's health bars
    health_bars_display()

    gameDisplay.blit(health_enemy.message_to_screen("Arrow keys to move", yellow, 30), [230, 530])
    gameDisplay.blit(health_enemy.message_to_screen("Space to attack", yellow, 30), [230, 550])
    gameDisplay.blit(health_enemy.message_to_screen("Top right corner x to exit", yellow, 30), [230, 570])

    pygame.display.update()

    # 60 fps
    clock.tick(60)

new_exit = False
enemy_obj.bolt_obj.run_lightning = False

link_win = pygame.image.load("link_win.png")
link_win = pygame.transform.scale(link_win, (104, 180))
link_win_rect = link_win.get_rect(center=(350, 350))

zelda = pygame.image.load("Zelda.png")
zelda = pygame.transform.scale(zelda, (64, 92))
zelda_rect = zelda.get_rect(center=(450, 400))

ganon_win = pygame.image.load("ganon_win.png")
ganon_win = pygame.transform.scale(ganon_win, (144, 126))
ganon_rect = ganon_win.get_rect(center=(350, 350))

link_dead = pygame.image.load("link_dead.png")
link_dead = pygame.transform.scale(link_dead, (96, 60))
link_dead_rect = link_dead.get_rect(center=(475, 385))

while not new_exit and not quit_button:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            new_exit = True

    if gameLose:
        gameDisplay.blit(sprite_obj.boss_map, (0, 0))
        gameDisplay.blit(health_player.message_to_screen("GAME OVER", black, 100), [190, 155])
        gameDisplay.blit(link_dead, link_dead_rect)
        gameDisplay.blit(ganon_win, ganon_rect)
        gameDisplay.blit(health_enemy.message_to_screen("Press the x on the top right corner to exit",
                                                        yellow, 50), [65, 550])
        pygame.display.update()
    elif gameWin:
        gameDisplay.blit(sprite_obj.boss_map, (0, 0))
        gameDisplay.blit(health_player.message_to_screen("YOU WIN", black, 100), [250, 155])
        gameDisplay.blit(link_win, link_win_rect)
        gameDisplay.blit(zelda, zelda_rect)
        gameDisplay.blit(health_enemy.message_to_screen("Press the x on the top right corner to exit",
                                                        yellow, 50), [65, 550])
        pygame.display.update()

pygame.quit()
quit()


# ah, link...it is you.
# you are the chosen one!
# link: unfortunately I am sigh
# save the princess. save the world.
# link: i know i know
# link: i have plenty of experience in this field of work
# good luck. you may enter and obtain the power of the master sword
