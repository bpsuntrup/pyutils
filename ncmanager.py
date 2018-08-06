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

if __name__ == "__main__":
    import time
    with NCurses() as nc:
        # Pick colors I like:
        nc.init_pair(1, nc.COLOR_RED, nc.COLOR_WHITE)
        nc.init_pair(2, nc.COLOR_WHITE, nc.COLOR_RED)
        nc.init_pair(3, nc.COLOR_BLUE, nc.COLOR_WHITE)
        nc.init_pair(4, nc.COLOR_BLUE, nc.COLOR_BLUE)
        nc.init_pair(5, nc.COLOR_GREEN, nc.COLOR_BLACK)
        nc.init_pair(6, nc.COLOR_BLACK, nc.COLOR_WHITE)

        # Draw a new window... I guess
        x = 0
        y = 0
        height = 40
        width = 40
        win = nc.newwin(height, width, y, x)
        win.timeout(200)
        win.addstr(2, 20, 'READY', nc.color_pair(3))
        win.refresh()
        time.sleep(2)
        win.addstr(4,20,'GO', nc.color_pair(2))
        win.refresh()

        
