#!/usr/bin/python
'''I'm bored. This is a venture into curses programming. Why
not?
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

  # Draw a new window... I guess
  x = 0
  y = 0
  height = 40
  width = 40
  win = curses.newwin(height, width, y, x)
  win.addstr('hi there ', curses.color_pair(3))
  win.refresh()
  time.sleep(1)
  win.addstr(4,0,'GO', curses.color_pair(2))
  win.refresh()
  
  #### Now the game begins ###
  y = 6
  x = 3
  snake_body = [(y, x),]
  FOOD = (random.randrange(height),random.randrange(width))

  # define a method for advancing the snake
  # todo: validate this is a good move... or not
  def advance(y,x):
    global snake_body
    global FOOD

    # clear window:
    for _y, _x in snake_body:
      win.addstr(_y,_x,' ', curses.color_pair(0))
    win.refresh()
      
    if (y,x) in snake_body:
      print 'you lose'
      exit(0)
    snake_body.append((y,x))
    if not (y,x) == FOOD:
      snake_body = snake_body[1:]
    else:
      while FOOD in snake_body:
        FOOD = (random.randrange(height),random.randrange(width))
      win.addstr(FOOD[0], FOOD[1],'*', curses.color_pair(5))
      win.refresh()

    # draw snake
    for _y, _x in snake_body:
      win.addstr(_y,_x,'*', curses.color_pair(4))
    win.refresh()


  # init the head and food
  win.addstr(y, x,'*', curses.color_pair(4))
  win.addstr(FOOD[0], FOOD[1],'*', curses.color_pair(5))
  win.refresh()
 
  while True:
    # Expecting an arrow key
    # Note that arrow keys are 3 bytes:
    # up:    27 91 65
    # down:  27 91 66
    # right: 27 91 67
    # left:  27 91 68
    if win.getch() == 27:
      if win.getch() == 91:
        move = win.getch()
        # up
        if move == 65:
          y -= 1
          advance(y,x)
        # down
        elif move == 66:
          y += 1
          advance(y,x)
        # right
        elif move == 67:
          x += 1
          advance(y,x)
        # left
        elif move == 68:
          x -= 1
          advance(y,x)

  time.sleep(1)

finally:
  # Leave this here. This cleans stuff up.
  curses.nocbreak(); stdscr.keypad(0); curses.echo()
  curses.endwin()
