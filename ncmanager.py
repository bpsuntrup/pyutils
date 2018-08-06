#!/usr/bin/python
'''
ncurses context manager
'''
import curses


class NCurses(object):
    """ncurses context manager"""
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        curses.curs_set(0)
    def __enter__(self):
        return curses

    def __exit__(self, *args):
        curses.nocbreak(); self.stdscr.keypad(0); curses.echo()
        curses.endwin()


class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

if __name__ == "__main__":
    import time
    with NCurses() as nc:
        # Pick colors I like:
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Draw a new window... I guess
        x = 0
        y = 0
        height = 40
        width = 40
        win = curses.newwin(height, width, y, x)
        win.timeout(200)
        win.addstr(2, 20, 'READY', curses.color_pair(3))
        win.refresh()
        time.sleep(2)
        win.addstr(4,20,'GO', curses.color_pair(2))
        win.refresh()

        
