# import the pygame module including the mixer for sounds
import pygame
pygame.mixer.init()
pygame.init()

# play the music for the main menu
pygame.mixer.music.load(r'E:\cyber_project\dojo_music.wav')
pygame.mixer.music.play(-1)

# lines 11 to 73 contain all the global variables
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SHOP_YELLOW = (181, 230, 29)

winner = 1

x = 230
y = 430
initial_x = 230
initial_y = 430
width = 40
height = 60
vel = 5
player_1_hp = 100
win_check_1 = 0
win_conditional_checker_1 = True
char_index_1 = 0
money_1 = 0
hp_potion_num_1 = 0
teleportation_potion_num_1 = 2
posess_camo_1 = 'No'
posess_ninja_1 = 'No'
damage_multiplier_1 = 1.0
base_damage_1 = 10

x2 = 1000
y2 = 430
initial_x2 = 1000
intial_y2 = 430
width2 = 40
height2 = 60
vel2 = 5
player_2_hp = 100
win_check_2 = 0
win_conditional_checker_2 = True
char_index_2 = 0
money_2 = 0
hp_potion_num_2 = 0
teleportation_potion_num_2 = 2
posess_camo_2 = 'No'
posess_ninja_2 = 'No'
damage_multiplier_2 = 1.0
base_damage_2 = 10


clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
looking_right_1 = True

isJump2 = False
jumpCount2 = 10

left2 = False
right2 = False
walkCount2 = 0
looking_right_2 = False

# lines 76 to 252 contain all of the images used in the game and the lists that represent the animations
IMAGE_BACK_INTRO = r'E:\cyber_project\Pictures\wp1.jpg'
intro_back_img = pygame.image.load(IMAGE_BACK_INTRO)

IMAGE_PUNCHING_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching.png'
punching_1_image = pygame.image.load(IMAGE_PUNCHING_1)
punching_1_image.set_colorkey(WHITE)

IMAGE_PUNCHING_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching.png'
punching_2_image = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_2), 1, 0)
punching_2_image.set_colorkey(WHITE)

IMAGE_PUNCHING_01 = r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\punching.png'
punching_01_image = pygame.image.load(IMAGE_PUNCHING_01)
punching_01_image.set_colorkey(WHITE)

IMAGE_PUNCHING_02 = r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\punching.png'
punching_02_image = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_02), 1, 0)
punching_02_image.set_colorkey(WHITE)

IMAGE_PUNCHING_CAMO_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_camo.png'
punching_camo_1_image = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_camo.png')
punching_camo_1_image.set_colorkey(WHITE)

IMAGE_PUNCHING_CAMO_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_camo.png'
punching_camo_2_image = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_camo.png'), 1, 0)
punching_camo_2_image.set_colorkey(WHITE)

IMAGE_PUNCHING_NINJA_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_ninja.png'
punching_ninja_1_image = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_ninja.png')
punching_ninja_1_image.set_colorkey(WHITE)

IMAGE_PUNCHING_NINJA_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_ninja.png'
punching_ninja_2_image = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\punching_ninja.png'), 1, 0)
punching_ninja_2_image.set_colorkey(WHITE)

IMAGE_AVATAR_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\avatar.png'
avatar_1_image = pygame.image.load(IMAGE_AVATAR_1)
avatar_1_image.set_colorkey(WHITE)

IMAGE_NINJA_AVATAR_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\ninja_avatar.png'
ninja_avatar_1_image = pygame.image.load(IMAGE_NINJA_AVATAR_1)
ninja_avatar_1_image.set_colorkey(WHITE)

IMAGE_AVATAR_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\avatar.png'
avatar_2_image = pygame.transform.flip(pygame.image.load(IMAGE_AVATAR_2), 1, 0)
avatar_2_image.set_colorkey(WHITE)

IMAGE_NAME_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\name.png'
name_1_image = pygame.image.load(IMAGE_NAME_1)
name_1_image.set_colorkey(WHITE)

IMAGE_NAME_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter2\name.png'
name_2_image = pygame.image.load(IMAGE_NAME_2)
name_2_image.set_colorkey(WHITE)

IMAGE_WIN_1 = r'E:\cyber_project\Pictures\fighter_templates\fighter1\win.png'
win_1_image = pygame.image.load(IMAGE_WIN_1)
win_1_image.set_colorkey(WHITE)

IMAGE_WIN_2 = r'E:\cyber_project\Pictures\fighter_templates\fighter2\win.png'
win_2_image = pygame.image.load(IMAGE_WIN_2)
win_2_image.set_colorkey(WHITE)

IMAGE_BLANK_HEALTHBAR = r'E:\cyber_project\Pictures\fighter_templates\blank_healthbar.png'
blank_healthbar_image = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\blank_healthbar.png')
blank_healthbar_image.set_colorkey(WHITE)

IMAGE_HP_POTION = r'E:\cyber_project\Pictures\hp_potion.png'
hp_potion_image = pygame.image.load(r'E:\cyber_project\Pictures\hp_potion.png')
hp_potion_image.set_colorkey(WHITE)

IMAGE_TELEPORTATION_POTION = r'E:\cyber_project\Pictures\teleportation_potion.png'
teleportation_potion_image = pygame.image.load(r'E:\cyber_project\Pictures\teleportation_potion.png')
teleportation_potion_image.set_colorkey(WHITE)

IMAGE_COINS = r'E:\cyber_project\Pictures\coins.png'
coins_image = pygame.image.load(r'E:\cyber_project\Pictures\coins.png')
coins_image.set_colorkey(WHITE)

IMAGE_RUNNING_LEFT_1 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1.png'), 1, 0)
IMAGE_RUNNING_LEFT_2 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2.png'), 1, 0)
IMAGE_RUNNING_LEFT_3 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3.png'), 1, 0)
IMAGE_RUNNING_LEFT_4 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4.png'), 1, 0)
IMAGE_RUNNING_LEFT_5 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5.png'), 1, 0)
IMAGE_RUNNING_LEFT_6 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6.png'), 1, 0)
IMAGE_RUNNING_LEFT_7 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7.png'), 1, 0)
IMAGE_RUNNING_LEFT_8 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8.png'), 1, 0)


IMAGE_RUNNING_LEFT_01 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_1.png'), 1, 0)
IMAGE_RUNNING_LEFT_02 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_2.png'), 1, 0)
IMAGE_RUNNING_LEFT_03 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_3.png'), 1, 0)
IMAGE_RUNNING_LEFT_04 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_4.png'), 1, 0)
IMAGE_RUNNING_LEFT_05 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_5.png'), 1, 0)
IMAGE_RUNNING_LEFT_06 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_6.png'), 1, 0)
IMAGE_RUNNING_LEFT_07 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_7.png'), 1, 0)
IMAGE_RUNNING_LEFT_08 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_8.png'), 1, 0)

IMAGE_RUNNING_LEFT_1_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_2_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_3_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_4_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_5_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_6_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_7_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7_camo.png'), 1, 0)
IMAGE_RUNNING_LEFT_8_CAMO = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8_camo.png'), 1, 0)

IMAGE_RUNNING_LEFT_1_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_2_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_3_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_4_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_5_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_6_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_7_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7_ninja.png'), 1, 0)
IMAGE_RUNNING_LEFT_8_NINJA = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8_ninja.png'), 1, 0)


win = pygame.display.set_mode((1400, 757))
pygame.display.set_caption("Brutal Fights")


walkRight = [pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8.png')]
walkLeft = [IMAGE_RUNNING_LEFT_1, IMAGE_RUNNING_LEFT_2, IMAGE_RUNNING_LEFT_3, IMAGE_RUNNING_LEFT_4, IMAGE_RUNNING_LEFT_5, IMAGE_RUNNING_LEFT_6, IMAGE_RUNNING_LEFT_7, IMAGE_RUNNING_LEFT_8]

walkRightCamo = [pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7_camo.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8_camo.png')]
walkLeftCamo = [IMAGE_RUNNING_LEFT_1_CAMO, IMAGE_RUNNING_LEFT_2_CAMO, IMAGE_RUNNING_LEFT_3_CAMO, IMAGE_RUNNING_LEFT_4_CAMO, IMAGE_RUNNING_LEFT_5_CAMO, IMAGE_RUNNING_LEFT_6_CAMO, IMAGE_RUNNING_LEFT_7_CAMO, IMAGE_RUNNING_LEFT_8_CAMO]
walkRightNinja = [pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_1_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_2_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_3_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_4_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_5_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_6_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_7_ninja.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\running_8_ninja.png')]
walkLeftNinja = [IMAGE_RUNNING_LEFT_1_NINJA, IMAGE_RUNNING_LEFT_2_NINJA, IMAGE_RUNNING_LEFT_3_NINJA, IMAGE_RUNNING_LEFT_4_NINJA, IMAGE_RUNNING_LEFT_5_NINJA, IMAGE_RUNNING_LEFT_6_NINJA, IMAGE_RUNNING_LEFT_7_NINJA, IMAGE_RUNNING_LEFT_8_NINJA]
char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png')
char_camo = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png')
char_ninja = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png')

walk_right_list = walkRight
walk_left_list = walkLeft

walkRight2 = [pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_1.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_2.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_3.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_4.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_5.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_6.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_7.png'), pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\running_8.png')]
walkLeft2 = [IMAGE_RUNNING_LEFT_01, IMAGE_RUNNING_LEFT_02, IMAGE_RUNNING_LEFT_03, IMAGE_RUNNING_LEFT_04, IMAGE_RUNNING_LEFT_05, IMAGE_RUNNING_LEFT_06, IMAGE_RUNNING_LEFT_07, IMAGE_RUNNING_LEFT_08]
char2 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png'), 1, 0)

walk_right_list_2 = walkRight2
walk_left_list_2 = walkLeft2

bg = pygame.image.load(r'E:\cyber_project\Pictures\fighting1.jpg')

intro_screen = pygame.display.set_mode((1400, 757))
IMAGE_BACK_INTRO = r'E:\cyber_project\Pictures\wp1.jpg'
intro_back_img = pygame.image.load(IMAGE_BACK_INTRO)


instructions_screen = pygame.display.set_mode((1400, 757))
IMAGE_BACK_INSTRUCTIONS = r'E:\cyber_project\Pictures\instructions.png'
instructions_back_image = pygame.image.load(IMAGE_BACK_INSTRUCTIONS)

shop_screen = pygame.display.set_mode((1400, 757))
IMAGE_BACK_SHOP = r'E:\cyber_project\Pictures\shop.png'
shop_back_image = pygame.image.load(IMAGE_BACK_SHOP)

winning_screen = pygame.display.set_mode((1400, 757))
IMAGE_BACK_WINNING = r'E:\cyber_project\Pictures\winning_background.jpg'
winning_back_image = pygame.image.load(IMAGE_BACK_WINNING)


winner_spot = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\blank_healthbar.png')

walkLeft[0].set_colorkey(WHITE)
walkLeft[1].set_colorkey(WHITE)
walkLeft[2].set_colorkey(WHITE)
walkLeft[3].set_colorkey(WHITE)
walkLeft[4].set_colorkey(WHITE)
walkLeft[5].set_colorkey(WHITE)
walkLeft[6].set_colorkey(WHITE)
walkLeft[7].set_colorkey(WHITE)
walkRight[0].set_colorkey(WHITE)
walkRight[1].set_colorkey(WHITE)
walkRight[2].set_colorkey(WHITE)
walkRight[3].set_colorkey(WHITE)
walkRight[4].set_colorkey(WHITE)
walkRight[5].set_colorkey(WHITE)
walkRight[6].set_colorkey(WHITE)
walkRight[7].set_colorkey(WHITE)
char.set_colorkey(WHITE)

punch_sound = pygame.mixer.Sound(r'E:\cyber_project\punch.wav')

run = True

##screen_var: 0 for intro, 1 for instructions, 2 for fights, 3 for store, 4 for winning
screen_var = 0


while run:
    clock.tick(24)  # how many frames per second the game will run on

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # a list the contains all the keys from the keyboard

    if keys[pygame.K_m] and screen_var != 2:  # lines 271 to 286 check if a key suitable for the screen was pressed and redirects the player to said screen
        screen_var = 0
        pygame.mixer.music.load(r'E:\cyber_project\dojo_music.wav')
        pygame.mixer.music.play(-1)
    if keys[pygame.K_i] and screen_var != 2:
        screen_var = 1
        pygame.mixer.music.load(r'E:\cyber_project\dojo_music.wav')
        pygame.mixer.music.play(-1)
    if keys[pygame.K_n] and screen_var != 2:
        screen_var = 3
        pygame.mixer.music.load(r'E:\cyber_project\dojo_music.wav')
        pygame.mixer.music.play(-1)
    if keys[pygame.K_KP_ENTER]:
        screen_var = 2
        pygame.mixer.music.load(r'E:\cyber_project\battle_music.wav')
        pygame.mixer.music.play(-1)

    if screen_var == 0:  # checks if the current screen is the main menu and prints the main menu on the screen
        intro_screen.blit(intro_back_img, (0, 0))
        pygame.display.flip()

    if screen_var == 1:  # checks if the current screen is the instructions screen and prints said screen
        instructions_screen.blit(instructions_back_image, (0, 0))
        pygame.display.flip()

    if screen_var == 2: # checks if the current screen is the fighting screen
        if char_index_1 == 1:  # checks the character for the first player and changes the damage multipliers accordingly
            damage_multiplier_2 = 0.8
        elif char_index_1 == 2:
            damage_multiplier_2 = 0.8
            damage_multiplier_1 = 1.5

        if char_index_2 == 1:  # checks the character for the second player and changes the damage multipliers accordingly
            damage_multiplier_1 = 0.8
        elif char_index_2 == 2:
            damage_multiplier_1 = 0.8
            damage_multiplier_2 = 1.5

        def redrawGameWindow():  # the redrawGameWindow fuction doesn't recieve any variables and is in charge of drawing the fighting screen
            # lines 311 to 240 are in charge of drawing the initial game window
            potion_font = pygame.font.SysFont('comicsans', 40, True)
            potion_text_1 = potion_font.render('X' + str(hp_potion_num_1), 1, BLACK)
            potion_text_2 = potion_font.render('X' + str(hp_potion_num_2), 1, BLACK)
            tele_text_1 = potion_font.render('X' + str(teleportation_potion_num_1), 1, BLACK)
            tele_text_2 = potion_font.render('X' + str(teleportation_potion_num_2), 1, BLACK)
            global walkCount
            global walkCount2
            global win_check_1
            global win_check_2
            win.blit(bg, (0, 0))
            if char_index_1 == 0 or char_index_1 == 1:
                win.blit(avatar_1_image, (20, 20))
            elif char_index_1 == 2:
                win.blit(ninja_avatar_1_image, (20, 20))
            if char_index_2 == 0 or char_index_2 == 1:
                win.blit(avatar_2_image, (1224, 20))
            elif char_index_2 == 2:
                win.blit(pygame.transform.flip(ninja_avatar_1_image, 1, 0), (1224, 20))
            win.blit(name_1_image, (186, 45))
            win.blit(name_2_image, (949, 45))
            win.blit(name_1_image, (x - 50, y - 50))
            win.blit(name_2_image, (x2 - 50, y2 - 50))
            win.blit(blank_healthbar_image, (195, 105))
            win.blit(blank_healthbar_image, (800, 105))
            pygame.draw.rect(win, RED, [195, 105, 400-((400/100) * (100-player_1_hp)), 30])
            pygame.draw.rect(win, BLACK, [195, 105, 400, 30], 5)
            pygame.draw.rect(win, RED, [800, 105, 400-((400/100) * (100-player_2_hp)), 30])
            pygame.draw.rect(win, BLACK, [800, 105, 400, 30], 5)
            win.blit(hp_potion_image, (180, 135))
            win.blit(potion_text_1, (230, 155))
            win.blit(hp_potion_image, (1110, 135))
            win.blit(potion_text_2, (1160, 155))
            win.blit(teleportation_potion_image, (300, 135))
            win.blit(tele_text_1, (350, 155))
            win.blit(teleportation_potion_image, (1000, 135))
            win.blit(tele_text_2, (1050, 155))

            # lines 343 to 367 are in charge of moving both characters according to the players' commands
            if walkCount + 1 >= 24:
                walkCount = 0

            if left:
                win.blit(walk_left_list[walkCount//3], (x, y))
                walkCount += 1
            elif right:
                win.blit(walk_right_list[walkCount//3], (x, y))
                walkCount += 1
            else:
                win.blit(char, (x, y))
                walkCount = 0

            if walkCount2 + 1 >= 24:
                walkCount2 = 0

            if left2:
                win.blit(walk_left_list_2[walkCount2//3], (x2, y2))
                walkCount2 += 1
            elif right2:
                win.blit(walk_right_list_2[walkCount2//3], (x2, y2))
                walkCount2 += 1
            else:
                win.blit(char2, (x2, y2))
                walkCount2 = 0

            pygame.display.update()  # updates the screen according to the movements, HP etc.

        # lines 372 to 487 are responsible for recieving  key presses from the first player and decide whether the first character should move left or right or execute a punch attack
        # each key-press conditional works just about the same: checks which skin is selected for the player and performs the action accordingly
        if keys[pygame.K_a] and x > 50:  # checks if the first player reached the left-hand side border
            x -= vel
            left = True
            right = False
            looking_right_1 = False
            if looking_right_1 is False and char_index_1 == 0:
                walk_left_list = walkLeft
            elif looking_right_1 is False and char_index_1 == 1:
                walk_left_list = walkLeftCamo
            elif looking_right_1 is False and char_index_1 == 2:
                walk_left_list = walkLeftNinja

        elif keys[pygame.K_d] and x < 1150:  # checks if the first player reached the right-hand side border
            x += vel
            left = False
            right = True
            looking_right_1 = True
            if looking_right_1 is True and char_index_1 == 0:
                walk_right_list = walkRight
            elif looking_right_1 is True and char_index_1 == 1:
                walk_right_list = walkRightCamo
            elif looking_right_1 is True and char_index_1 == 2:
                walk_right_list = walkRightNinja

        elif keys[pygame.K_g] and (looking_right_1 is True):
                if char_index_1 == 0:
                    char = pygame.image.load(IMAGE_PUNCHING_1)
                elif char_index_1 == 1:
                    char = pygame.image.load(IMAGE_PUNCHING_CAMO_1)
                elif char_index_1 == 2:
                    char = pygame.image.load(IMAGE_PUNCHING_NINJA_1)
                if x + 201 > x2 and x2 > x and x2 < x + 201:
                    print "player 1 hit player 2 from the left"
                    punch_sound.play()
                    if player_2_hp > 0:
                        player_2_hp -= (base_damage_1 * damage_multiplier_1)
                        x2 += 150
                        if x2 > 1150:
                            x2 = 1150
                    elif player_2_hp == 0 or player_2_hp < 0:  # if the second character dies, reinitializes the game screen
                        screen_var = 4
                        pygame.mixer.music.load(r'E:\cyber_project\gong.wav')
                        pygame.mixer.music.play(0)
                        winner = 1
                        money_1 += 100
                        money_2 += 25
                        x = initial_x
                        x2 = initial_x2
                        looking_right_1 = True
                        looking_right_2 = False
                        player_1_hp = 100
                        player_2_hp = 100
                        teleportation_potion_num_1 = 2

        elif keys[pygame.K_g] and (looking_right_1 is False):
                if char_index_1 == 0:
                    char = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_1), 1, 0)
                elif char_index_1 == 1:
                    char = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_CAMO_1), 1, 0)
                elif char_index_1 == 2:
                    char = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_NINJA_1), 1, 0)
                if x > x2 and x < x2 + 201:
                    print "player 1 hit player 2 from the right"
                    punch_sound.play()
                    if player_2_hp > 0:
                        player_2_hp -= (base_damage_1 * damage_multiplier_1)
                        x2 -= 150
                        if x2 < 50:
                            x2 = 50
                    elif player_2_hp == 0 or player_2_hp < 0:
                        screen_var = 4
                        pygame.mixer.music.load(r'E:\cyber_project\gong.wav')
                        pygame.mixer.music.play(0)
                        winner = 1
                        money_1 += 100
                        money_2 += 25
                        x = initial_x
                        x2 = initial_x2
                        looking_right_1 = True
                        looking_right_2 = False
                        player_1_hp = 100
                        player_2_hp = 100
                        teleportation_potion_num_1 = 2

        elif keys[pygame.K_h]:  # checks if the player use the HP potion and acts accordingly
            if hp_potion_num_1 > 0:
                hp_potion_num_1 -= 1
                player_1_hp += 30
                if player_1_hp > 100:
                    player_1_hp = 100

        elif keys[pygame.K_t]: # checks if the player use the teleportation potion and acts accordingly
            if teleportation_potion_num_1 > 0:
                if x < x2 and x2 < 900:
                    x = x2 + 150
                    teleportation_potion_num_1 -= 1
                elif x > x2 and x2 > 300:
                    x = x2 - 150
                    teleportation_potion_num_1 -= 1

        else:  # if the player is stationary prints the suitable character
            left = False
            right = False
            walkCount = 0
            if looking_right_1 is True and char_index_1 == 0:
                char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png')
            elif looking_right_1 is True and char_index_1 == 1:
                char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png')
            elif looking_right_1 is True and char_index_1 == 2:
                char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png')
            elif looking_right_1 is False and char_index_1 == 0:
                char = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png'), 1, 0)
            elif looking_right_1 is False and char_index_1 == 1:
                char = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), 1, 0)
            elif looking_right_1 is False and char_index_1 == 2:
                char = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), 1, 0)

        if not(isJump):  # checks if the player pressed the jump key and moves him accordingly
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False

        # lines 505 to 636 work exactly the same like 372 to 502, just for player 2 instead of player 1
        if keys[pygame.K_LEFT] and x2 > 50:
            x2 -= vel2
            left2 = True
            right2 = False
            looking_right_2 = False
            if looking_right_2 is False and char_index_2 == 0:
                walk_left_list_2 = walkLeft2
            elif looking_right_2 is False and char_index_2 == 1:
                walk_left_list_2 = walkLeftCamo
            elif looking_right_2 is False and char_index_2 == 2:
                walk_left_list_2 = walkLeftNinja

        elif keys[pygame.K_RIGHT] and x2 < 1150:
            x2 += vel2
            left2 = False
            right2 = True
            looking_right_2 = True
            if looking_right_2 is True and char_index_2 == 0:
                walk_right_list_2 = walkRight2
            elif looking_right_2 is True and char_index_2 == 1:
                walk_right_list_2 = walkRightCamo
            elif looking_right_2 is True and char_index_2 == 2:
                walk_right_list_2 = walkRightNinja

        elif keys[pygame.K_p] and (looking_right_2 is True):
                if char_index_2 == 0:
                    char2 = pygame.image.load(IMAGE_PUNCHING_01)
                elif char_index_2 == 1:
                    char2 = pygame.image.load(IMAGE_PUNCHING_CAMO_1)
                elif char_index_2 == 2:
                    char2 = pygame.image.load(IMAGE_PUNCHING_NINJA_1)
                if x2 + 201 > x and x2 + 201 < x + 201 and x > x2:
                    print "player 2 hit player 1 from the left"
                    punch_sound.play()
                    if player_1_hp > 0:
                        player_1_hp -= (base_damage_2 * damage_multiplier_2)
                        x += 150
                        if x > 1150:
                            x = 1150
                    elif player_1_hp == 0 or player_1_hp < 0:
                        screen_var = 4
                        pygame.mixer.music.load(r'E:\cyber_project\gong.wav')
                        pygame.mixer.music.play(0)
                        winner = 2
                        money_1 += 25
                        money_2 += 100
                        x = initial_x
                        x2 = initial_x2
                        looking_right_1 = True
                        looking_right_2 = False
                        player_1_hp = 100
                        player_2_hp = 100
                        teleportation_potion_num_1 = 2

        elif keys[pygame.K_p] and (looking_right_2 is False):
                if char_index_2 == 0:
                    char2 = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_01), 1, 0)
                elif char_index_2 == 1:
                    char2 = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_CAMO_1), 1, 0)
                elif char_index_2 == 2:
                    char2 = pygame.transform.flip(pygame.image.load(IMAGE_PUNCHING_NINJA_1), 1, 0)
                if x2 > x and x2 < x + 201 and x2 + 201 > x + 201:
                    print "player 2 hit player 1 from the right"
                    punch_sound.play()
                    if player_1_hp > 0:
                        player_1_hp -= (base_damage_2 * damage_multiplier_2)
                        x -= 150
                        if x < 50:
                            x = 50
                    elif player_1_hp == 0 or player_1_hp < 0:
                        screen_var = 4
                        pygame.mixer.music.load(r'E:\cyber_project\gong.wav')
                        pygame.mixer.music.play(0)
                        winner = 2
                        money_1 += 25
                        money_2 += 100
                        x = initial_x
                        x2 = initial_x2
                        looking_right_1 = True
                        looking_right_2 = False
                        player_1_hp = 100
                        player_2_hp = 100
                        teleportation_potion_num_1 = 2

        elif keys[pygame.K_i]:
            if hp_potion_num_2 > 0:
                hp_potion_num_2 -= 1
                player_2_hp += 30
                if player_2_hp > 100:
                    player_2_hp = 100

        elif keys[pygame.K_o]:
            if teleportation_potion_num_2 > 0:
                if x2 < x and x < 900:
                    x2 = x + 150
                    teleportation_potion_num_2 -= 1
                elif x2 > x and x > 300:
                    x2 = x - 150
                    teleportation_potion_num_2 -= 1

        else:
            left2 = False
            right2 = False
            walkCount2 = 0
            if looking_right_2 is True and char_index_2 == 0:
                char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png')
            elif looking_right_2 is True and char_index_2 == 1:
                char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png')
            elif looking_right_2 is True and char_index_2 == 2:
                char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png')
            elif looking_right_2 is False and char_index_2 == 0:
                char2 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png'), 1, 0)
            elif looking_right_2 is False and char_index_2 == 1:
                char2 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), 1, 0)
            elif looking_right_2 is False and char_index_2 == 2:
                char2 = pygame.transform.flip(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), 1, 0)


        if not(isJump2):
            if keys[pygame.K_UP]:
                isJump2 = True
                left2 = False
                right2 = False
                walkCount2 = 0
        else:
            if jumpCount2 >= -10:
                y2 -= (jumpCount2 * abs(jumpCount2)) * 0.5
                jumpCount2 -= 1
            else:
                jumpCount2 = 10
                isJump2 = False
        redrawGameWindow()

    if screen_var == 3:  # lines 639 to 713 are responsible for printing the shop screen
        font = pygame.font.SysFont('comicsans', 30, True)
        money_1_text = font.render(str(money_1), 1, WHITE)
        money_2_text = font.render(str(money_2), 1, WHITE)
        missing_money_1_text = font.render('Not enough gold for Player 1', 1, WHITE)
        missing_money_2_text = font.render('Not enough gold for Player 2', 1, WHITE)
        max_potions_text = font.render('Max amount of potions reached', 1, WHITE)
        price_camo = font.render('75 Gold', 1, WHITE)
        price_ninja = font.render('200 Gold', 1, WHITE)
        price_potion = font.render('50 Gold', 1, WHITE)
        inventory_1_text_1 = font.render('Inventory:', 1, WHITE)
        inventory_1_text_2 = font.render('HP Potions: ' + str(hp_potion_num_1), 1, WHITE)
        inventory_1_text_3 = font.render('Camo Skin: ' + posess_camo_1, 1, WHITE)
        inventory_1_text_4 = font.render('Ninja Skin: ' + posess_ninja_1, 1, WHITE)
        inventory_2_text_1 = font.render('Inventory:', 1, WHITE)
        inventory_2_text_2 = font.render('HP Potions: ' + str(hp_potion_num_2), 1, WHITE)
        inventory_2_text_3 = font.render('Camo Skin: ' + posess_camo_2, 1, WHITE)
        inventory_2_text_4 = font.render('Ninja Skin: ' + posess_ninja_2, 1, WHITE)
        if char_index_1 == 0:
            char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png')
        if char_index_1 == 1:
            char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png')
        if char_index_1 == 2:
            char = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png')
        if char_index_2 == 0:
            char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png')
        if char_index_2 == 1:
            char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png')
        if char_index_2 == 2:
            char2 = pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png')
        shop_screen.blit(shop_back_image, (0, 0))
        shop_screen.blit(inventory_1_text_1, (380, 230))
        shop_screen.blit(inventory_1_text_2, (380, 260))
        shop_screen.blit(inventory_1_text_3, (380, 290))
        shop_screen.blit(inventory_1_text_4, (380, 320))
        pygame.draw.rect(win, WHITE, [370, 210, 200, 150], 3)
        shop_screen.blit(inventory_2_text_1, (1000, 230))
        shop_screen.blit(inventory_2_text_2, (1000, 260))
        shop_screen.blit(inventory_2_text_3, (1000, 290))
        shop_screen.blit(inventory_2_text_4, (1000, 320))
        pygame.draw.rect(win, WHITE, [990, 210, 200, 150], 3)
        pygame.draw.rect(win, SHOP_YELLOW, [210, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [210, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png'), (65, 155)), (235, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [365, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [365, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), (65, 155)), (390, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [520, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [520, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), (65, 155)), (545, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [855, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [855, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png'), (65, 155)), (880, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [1005, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [1005, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), (65, 155)), (1030, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [1160, 455, 115, 170])
        pygame.draw.rect(win, WHITE, [1160, 455, 115, 170], 3)
        win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), (65, 155)), (1185, 460))
        pygame.draw.rect(win, SHOP_YELLOW, [30, 295, 150, 330])
        pygame.draw.rect(win, WHITE, [30, 295, 150, 330], 3)
        win.blit(pygame.transform.scale(char, (130, 310)), (40, 300))
        pygame.draw.rect(win, SHOP_YELLOW, [675, 295, 150, 330])
        pygame.draw.rect(win, WHITE, [675, 295, 150, 330], 3)
        win.blit(pygame.transform.scale(char2, (130, 310)), (685, 300))
        pygame.draw.rect(win, SHOP_YELLOW, [225, 290, 50, 50])
        pygame.draw.rect(win, WHITE, [225, 290, 50, 50], 3)
        shop_screen.blit(hp_potion_image, (220, 285))
        pygame.draw.rect(win, SHOP_YELLOW, [850, 290, 50, 50])
        pygame.draw.rect(win, WHITE, [850, 290, 50, 50], 3)
        shop_screen.blit(hp_potion_image, (845, 285))
        shop_screen.blit(coins_image, (50, 220))
        shop_screen.blit(money_1_text, (100, 235))
        shop_screen.blit(coins_image, (680, 220))
        shop_screen.blit(money_2_text, (730, 235))
        mouse_x, mouse_y = pygame.mouse.get_pos()  # lines 713 to to 743 are responsible for checking if the player's cursor is hovering over an item and represents the item's price
        if mouse_x > 225 and mouse_x < 275 and mouse_y > 290 and mouse_y < 340:
            pygame.draw.rect(win, (153, 217, 234), [225, 290, 50, 50])
            win.blit(hp_potion_image, (220, 285))
            shop_screen.blit(price_potion, (375, 680))
        if mouse_x > 850 and mouse_x < 900 and mouse_y > 290 and mouse_y < 340:
            pygame.draw.rect(win, (153, 217, 234), [850, 290, 50, 50])
            win.blit(hp_potion_image, (845, 285))
            shop_screen.blit(price_potion, (1025, 680))
        if mouse_x > 210 and mouse_x < 325 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [210, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing.png'), (65, 155)), (235, 460))
        if mouse_x > 365 and mouse_x < 480 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [365, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), (65, 155)), (390, 460))
            shop_screen.blit(price_camo, (375, 680))
        if mouse_x > 520 and mouse_x < 635 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [520, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), (65, 155)), (545, 460))
            shop_screen.blit(price_ninja, (365, 680))
        if mouse_x > 855 and mouse_x < 970 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [855, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter2\right\standing.png'), (65, 155)), (880, 460))
        if mouse_x > 1005 and mouse_x < 1120 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [1005, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_camo.png'), (65, 155)), (1030, 460))
            shop_screen.blit(price_camo, (1025, 680))
        if mouse_x > 1160 and mouse_x < 1285 and mouse_y > 455 and mouse_y < 625:
            pygame.draw.rect(win, (153, 217, 234), [1160, 455, 115, 170])
            win.blit(pygame.transform.scale(pygame.image.load(r'E:\cyber_project\Pictures\fighter_templates\fighter1\right\standing_ninja.png'), (65, 155)), (1185, 460))
            shop_screen.blit(price_ninja, (1015, 680))
        if event.type == pygame.MOUSEBUTTONDOWN:  # checks if the player pressed the mouse and lets or doesn't lets the player purchase the wanted item
            if mouse_x > 225 and mouse_x < 275 and mouse_y > 290 and mouse_y < 340:
                if money_1 >= 50:
                    money_1 -= 50
                    if hp_potion_num_1 < 2:
                        hp_potion_num_1 += 1
                        swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                        swords.play()
                    else:
                        shop_screen.blit(max_potions_text, (250, 720))
                else:
                    shop_screen.blit(missing_money_1_text, (250, 720))
            if mouse_x > 850 and mouse_x < 900 and mouse_y > 290 and mouse_y < 340:
                if money_2 >= 50:
                    money_2 -= 50
                    if hp_potion_num_2 < 2:
                        hp_potion_num_2 += 1
                        swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                        swords.play()
                    else:
                        shop_screen.blit(max_potions_text, (250, 720))
                else:
                    shop_screen.blit(missing_money_2_text, (900, 720))
            if mouse_x > 210 and mouse_x < 325 and mouse_y > 455 and mouse_y < 625:
                char_index_1 = 0
            if mouse_x > 365 and mouse_x < 480 and mouse_y > 455 and mouse_y < 625:
                if money_1 >= 75:
                    money_1 -= 75
                    char_index_1 = 1
                    posess_camo_1 = 'Yes'
                    swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                    swords.play()
                else:
                    shop_screen.blit(missing_money_1_text, (250, 720))
            if mouse_x > 520 and mouse_x < 635 and mouse_y > 455 and mouse_y < 625:
                if money_1 >= 200:
                    money_1 -= 200
                    char_index_1 = 2
                    posess_ninja_1 = 'Yes'
                    swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                    swords.play()
                else:
                    shop_screen.blit(missing_money_1_text, (250, 720))
            if mouse_x > 855 and mouse_x < 970 and mouse_y > 455 and mouse_y < 625:
                char_index_2 = 0
            if mouse_x > 1005 and mouse_x < 1120 and mouse_y > 455 and mouse_y < 625:
                if money_2 >= 75:
                    money_2 -= 75
                    char_index_2 = 1
                    posess_camo_2 = 'Yes'
                    swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                    swords.play()
                else:
                    shop_screen.blit(missing_money_2_text, (900, 720))
            if mouse_x > 1160 and mouse_x < 1285 and mouse_y > 455 and mouse_y < 625:
                if money_2 >= 200:
                    money_2 -= 200
                    char_index_2 = 2
                    posess_ninja_2 = 'Yes'
                    swords = pygame.mixer.Sound(r'E:\cyber_project\swords.wav')
                    swords.play()
                else:
                    shop_screen.blit(missing_money_2_text, (900, 720))
        pygame.display.flip()

    if screen_var == 4:  # a screen that is responsible for declaring the winner of the fight
        winning_screen.blit(winning_back_image, (0, 0))
        if winner == 1:
            winning_screen.blit(win_1_image, (260, 330))
        if winner == 2:
            winning_screen.blit(win_2_image, (250, 330))
        pygame.display.flip()


pygame.quit()