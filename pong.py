# Author: Rehoboth Okorie
# Date: 27th Jan 2020
# Purpose: Pong game

from cs1lib import *
from random import *

# to restart the game
restart = False
restart_count = 0

# score count
p1_score = 0
p2_score = 0
winner = ""

# variables to control the direction of the paddles
r_up = False
l_up = False
l_down = False
r_down = False

# variables to track the location of paddles
y_right_paddle = 175
y_left_paddle = 175

# variables to track the direction of the ball
x_list_velocity = [2, -2]
y_list_velocity = [1, -1, 1.5, -1.5, 0.5, -0.5]
x_velocity = choice(x_list_velocity)
y_velocity = choice(y_list_velocity)

# variables to track the location of the pong ball
ball_center_y = 200
ball_center_x = 200
r = 1
g = 0.5
b = 1

# necessary for condition to set background color
background_cond = 1


# to quit the game
def quit_pong():
    cs1_quit()


# displays game over message
def game_over():
    global winner

    # if left paddle wins
    if ball_center_x > 390:
        winner = "p1"
        clear()
        set_font_size(24)
        draw_text("Game Over!", 130, 200)
        draw_text("p1 WINS!", 155, 230)

    # if right paddle wins
    elif ball_center_x < 10:
        winner = "p2"
        clear()
        set_font_size(24)
        draw_text("Game Over!", 130, 200)
        draw_text("p2 WINS!", 155, 230)


# restart function to reset all necessary variables
def restart_func():
    global restart, r_up, r_down, l_up, l_down, y_right_paddle
    global y_left_paddle, ball_center_x, ball_center_y
    global background_cond, x_velocity, y_velocity, restart_count
    global p1_score, p2_score

    if winner == "p1":
        p1_score += 1
    elif winner == "p2":
        p2_score += 1
    clear()
    # to restart the game
    restart = False
    restart_count = 0

    # variables to control the direction of the paddles
    r_up = False
    l_up = False
    l_down = False
    r_down = False

    # variables to track the location of paddles
    y_right_paddle = 175
    y_left_paddle = 175

    # variables to track the direction of the ball
    x_velocity = choice(x_list_velocity)
    y_velocity = choice(y_list_velocity)

    # variables to track the location of the pong ball
    ball_center_y = 200
    ball_center_x = 200

    # necessary for condition to set background color
    background_cond = 1


def score_draw():
    set_font_size(20)
    draw_text(str(p1_score), 5, y_left_paddle + 45)
    draw_text(str(p2_score), 385, y_right_paddle + 45)


# function to draw the ball
def ball():
    global ball_center_x, ball_center_y, r, g, b
    # prevents draw overlap
    clear()
    # draws ball
    set_fill_color(r, g, b)
    draw_circle(ball_center_x, ball_center_y, 9)
    # updates position of the ball
    ball_center_x += x_velocity
    ball_center_y += y_velocity


# controls changing components of ball velocity
def ball_velocity():
    global x_velocity, y_velocity, r, g, b

    # control the and increase velocity of ball on collision with paddles
    if ball_center_x >= 370 and not (ball_center_y < y_right_paddle - 10 or ball_center_y > y_right_paddle + 95):
        x_velocity = -x_velocity
        y_velocity = choice(y_list_velocity)
        r, g, b = uniform(0, 1), uniform(0, 1), uniform(0, 1)

    elif ball_center_x <= 30 and not (ball_center_y < y_left_paddle - 10 or ball_center_y > y_left_paddle + 95):
        x_velocity = -x_velocity
        y_velocity = choice(y_list_velocity)
        r, g, b = uniform(0, 1), uniform(0, 1), uniform(0, 1)

    if ball_center_y <= 10:
        y_velocity = -y_velocity
    elif ball_center_y >= 390:
        y_velocity = -y_velocity


# movement dynamics of the paddles
def paddle_move():
    global y_right_paddle, y_left_paddle

    if l_up and y_left_paddle >= 0:
        y_left_paddle -= 2.5

    if l_down and y_left_paddle <= 310:
        y_left_paddle += 2.5

    if r_up and y_right_paddle >= 0:
        y_right_paddle -= 2.5

    if r_down and y_right_paddle <= 310:
        y_right_paddle += 2.5


# get and manages key presses
def keypress(direct):
    global y_left_paddle, restart, y_right_paddle
    global ball_center_x, l_up, r_up, r_down, l_down, restart_count

    # key presses to direct the paddles
    if direct.lower() == "a":
        l_up = True
    elif direct.lower() == "z":
        l_down = True

    if direct.lower() == "k":
        r_up = True
    elif direct.lower() == "m":
        r_down = True

    if direct.lower() == " ":
        restart = True
        if restart_count <= 2:
            restart_count += 1
    if direct.lower() == "q":
        quit_pong()


# manages key releases
def keyrelease(direct):
    global l_up, r_up, r_down, l_down, restart

    if direct.lower() == "a":
        l_up = False
    elif direct.lower() == "z":
        l_down = False

    if direct.lower() == "k":
        r_up = False
    elif direct.lower() == "m":
        r_down = False


# the actual main draw space
def main_draw():
    # get background_cond to function for ues
    global background_cond

    # condition that set background only once
    if background_cond == 1:
        set_clear_color(1, 1, 0)
        clear()
        background_cond = 2

    ball()
    ball_velocity()
    paddle_move()
    # first paddle
    set_fill_color(1, 0, 0)
    draw_rectangle(0, y_left_paddle, 20, 90)

    # 2nd paddle
    set_fill_color(1, 0, 0)
    draw_rectangle(380, y_right_paddle, 20, 90)


# function called in start_graphics; controls finals flow control logistics
def pong():
    global restart, x_velocity, y_velocity

    if 10 < ball_center_x or ball_center_x < 390:
        if not restart:
            main_draw()
    if 10 > ball_center_x or ball_center_x > 390:
        x_velocity, y_velocity = 0, 0

    if restart:
        if restart_count < 2:
            clear()
            game_over()
        else:
            restart_func()
    score_draw()

start_graphics(pong, framerate=80, key_press=keypress, key_release=keyrelease)
