# Last Dream-Roguelike RPG by Распутин

import curses
from player import *

KEY_ESC = 27

def main(stdscr):
    curses.noecho()                            # Do not echo keys onto screen
    curses.cbreak()                            # Accept key without ENTER
    stdscr.keypad(True)                        # Enable keypad
    stdscr.clear()                             # Clear screen
    player = Player("@", curses.COLOR_RED, 50) # Player settings
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    player_color_pair = curses.color_pair(1)

    # Get the screen size
    screen_height, screen_width = stdscr.getmaxyx()
    
    # Define main window
    win_height = 25
    win_width = screen_width
    win_start_y = 0
    win_start_x = 0
    stdscr.refresh()

    # Ensure the main window fits within the screen
    win_height = min(win_height, screen_height - 5)
    win_width = min(win_width, screen_width)

    # Create a new window
    win = curses.newwin(win_height, win_width, win_start_y, win_start_x)
    win.border()
    

    # Initial position of the string
    string_y = 1
    string_x = 1
    win.addstr(string_y, string_x, player.player_character, player_color_pair)
    win.refresh()

    # Message window settings
    msg_win_height = 5
    msg_win_width = screen_width  # Ensure the message window fits within the screen width
    msg_win_start_y = win_height  # Start just below the main window
    msg_win_start_x = 0

    # Print debugging information
    #stdscr.addstr(screen_height - 1, 0, f"Screen: {screen_height}x{screen_width}, Main Win: {win_height}x{win_width}, Msg Win: {msg_win_height}x{msg_win_width} at ({msg_win_start_y},{msg_win_start_x})")

    # Create the message window
    msg_win = curses.newwin(msg_win_height, msg_win_width, msg_win_start_y, msg_win_start_x)
    msg_win.border()
    msg_win.addstr(1, 1, f"Health: {player.player_health}")
    msg_win.refresh()

    # Main loop to wait for key press
    while True:
        key = stdscr.getch()

        if key == KEY_ESC:
            break
        elif key == curses.KEY_UP and string_y > 1:
            string_y -= 1
        elif key == curses.KEY_DOWN and string_y < win_height - 2:
            string_y += 1
        elif key == curses.KEY_LEFT and string_x > 1:
            string_x -= 1
        elif key == curses.KEY_RIGHT and string_x < win_width - len(player.player_character) - 1:
            string_x += 1

        # Clear the window and update the string position
        win.clear()
        win.border()
        win.addstr(string_y, string_x, player.player_character, player_color_pair)
        win.refresh()
        msg_win.refresh()  # Refresh the message window

        # Update the message window with the player's health
        msg_win.clear()  # Highlighted Change
        msg_win.border()  # Highlighted Change
        msg_win.addstr(1, 1, f"Health: {player.player_health}")  # Highlighted Change
        msg_win.refresh()  # Highlighted Change

    # Restore terminal settings
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

# Run the main function using curses.wrapper
curses.wrapper(main)
