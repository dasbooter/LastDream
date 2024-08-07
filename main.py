#Last Dream-Rougelike RPG by Распутин

import time
import curses
from curses import wrapper
stdscr = curses.initscr() #Initialize curses library
curses.echo()             #Echo keys onto screen
curses.nocbreak()         #Accept key without ENTER
stdscr.keypad(True)       #Enable keypad
time.sleep(5)             #Wait for 5 seconds
curses.endwin()           #Close curses window

