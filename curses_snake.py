#!/usr/bin/python
'''I'm bored. This is a venture into curses programming. Why
not?

To run, simply `python curses_snake.py`

Don't work, open an issue.
'''
import curses
import time
import random

try:
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    curses.curs_set(0)

    # Pick colors I like:
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Draw a new window... I guess
    HEIGHT = 40
    WIDTH = 40
    WIN = curses.newwin(HEIGHT, WIDTH, 0, 0)
    WIN.timeout(200)
    WIN.addstr(2, 20, 'READY', curses.color_pair(3))
    WIN.refresh()
    time.sleep(2)
    WIN.addstr(4, 20, 'GO', curses.color_pair(2))
    WIN.refresh()

    #### Now the game begins ###
    y = 6
    x = 3
    SNAKE_BODY = [(y, x),]
    FOOD = (random.randrange(HEIGHT), random.randrange(WIDTH))
    BOUNDARY = [(0, i) for i in range(WIDTH-1)]
    BOUNDARY += [(HEIGHT-1, i) for i in range(WIDTH-1)]
    BOUNDARY += [(i, 0) for i in range(HEIGHT-1)]
    BOUNDARY += [(i, WIDTH-1) for i in range(HEIGHT-1)]
    SCORE = 0
    DIRECTION = 'down'

    # define a method for advancing the snake
    # todo: validate this is a good move... or not
    def advance(y,x):
        global SNAKE_BODY
        global FOOD
        global SCORE

        # clear window:
        for _y, _x in SNAKE_BODY:
            WIN.addstr(_y,_x,' ', curses.color_pair(0))
        WIN.refresh()

        if (y,x) in SNAKE_BODY or (y,x) in BOUNDARY:
            WIN.addstr(4,20,'SCORE: {}'.format(SCORE), curses.color_pair(1))
            WIN.refresh()
            time.sleep(3)
            exit(0)
        SNAKE_BODY.append((y,x))
        if not (y,x) == FOOD:
            SNAKE_BODY = SNAKE_BODY[1:]
        else:
            SCORE += 1
            WIN.addstr(0,2,str(SCORE), curses.color_pair(6))
            while FOOD in SNAKE_BODY or FOOD in BOUNDARY:
                FOOD = (random.randrange(HEIGHT),random.randrange(WIDTH))
            WIN.addstr(FOOD[0], FOOD[1],'*', curses.color_pair(5))
            WIN.refresh()

        # draw snake
        for _y, _x in SNAKE_BODY:
            WIN.addstr(_y,_x,'*', curses.color_pair(4))
        WIN.refresh()

    # init the head and food and SCORE
    WIN.addstr(y, x,'*', curses.color_pair(4))
    WIN.addstr(FOOD[0], FOOD[1],'*', curses.color_pair(5))
    for coord in BOUNDARY:
        WIN.addstr(coord[0], coord[1], ' ', curses.color_pair(6))
    WIN.addstr(0,2,str(SCORE), curses.color_pair(6))
    WIN.refresh()

    while True:
        # Expecting an arrow key
        # Note that arrow keys are 3 bytes:
        # up:        27 91 65
        # down:    27 91 66
        # right: 27 91 67
        # left:    27 91 68
        try:
            move = WIN.getch()
        except:
            move = -1
        if move == 27:
            if WIN.getch() == 91:
                move = WIN.getch()
                # up
                if move == 65:
                    y -= 1
                    DIRECTION = 'up'
                    advance(y,x)
                # down
                elif move == 66:
                    y += 1
                    DIRECTION = 'down'
                    advance(y,x)
                # right
                elif move == 67:
                    x += 1
                    DIRECTION = 'right'
                    advance(y,x)
                # left
                elif move == 68:
                    x -= 1
                    DIRECTION = 'left'
                    advance(y,x)
        elif move == -1:
            if DIRECTION == 'up':
                y -= 1
                advance(y,x)
            if DIRECTION == 'down':
                y += 1
                advance(y,x)
            if DIRECTION == 'right':
                x += 1
                advance(y,x)
            if DIRECTION == 'left':
                x -= 1
                advance(y,x)

    time.sleep(1)

finally:
    # Leave this here. This cleans stuff up.
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()
