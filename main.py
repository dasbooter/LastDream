#Last Dream-Rougelike RPG by Распутин

import curses

def main(stdscr):
    # Initialize curses settings
    curses.cbreak()           # React to keys instantly without needing Enter
    stdscr.keypad(True)       # Enable special keys to be captured (arrows, etc.)
    curses.noecho()           # Disable echoing of keys to the screen

    # Clear the screen at the start
    stdscr.clear()

    # Define the window size and position
    win_height = 30
    win_width = 140
    win_start_y = 0
    win_start_x = 0

    # Create a new window
    win = curses.newwin(win_height, win_width, win_start_y, win_start_x)
    win2 = curses.newwin(10, win_width, 30, win_start_x)

    # Add a border to the window
    win.border()
    win2.border()

    # Add a string to the window
    win.addstr(1, 1, "Привет, example text.")
    win2.addstr(1, 1, "Second test.")

    # Refresh the window to display changes
    win.refresh()

    # Wait for 5 seconds or until a key press
    win.timeout(5000)      # Set a timeout of 5000 milliseconds (5 seconds)
    win.getch()            # Wait for a key press or timeout

    # Restore terminal settings
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

# Run the main function using curses.wrapper
curses.wrapper(main)
