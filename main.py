# Last Dream-Roguelike RPG by Распутин

import curses
from player import *
from creatures import Creature
from races import Race
from character_classes import CharacterClass

KEY_ESC = 27
KEY_CHARACTER = ord('c')
KEY_CLOSE = ord(' ')

def main(stdscr):
    curses.noecho()                            # Do not echo keys onto screen
    curses.cbreak()                            # Accept key without ENTER
    stdscr.keypad(True)                        # Enable keypad
    stdscr.clear()                             # Clear screen
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    player_color_pair = curses.color_pair(1)

    # Race and class options
    races = ["Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Tiefling"]
    classes = ["Fighter", "Wizard", "Cleric"]

    selected_race = select_option(stdscr, "Select Race", races)
    selected_class = select_option(stdscr, "Select Class", classes)
    player_name = get_player_name(stdscr)

    # Create the player character with default attributes
    player = CharacterClass(player_name, 10, 10, 10, 10, 10, 10, selected_race, selected_class)

    # Display the main game window
    display_main_window(stdscr, player)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

def select_option(stdscr, prompt, options):
    current_row = 0
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    while True:
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx + 1, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, option)
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_row]
        elif key == KEY_ESC:
            curses.endwin()
            exit()

def get_player_name(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter your name: ")
    stdscr.refresh()
    curses.echo()
    player_name = stdscr.getstr(0, len("Enter your name: ") + 1, 20).decode('utf-8')
    curses.noecho()
    return player_name

def display_main_window(stdscr, player):
    stdscr.clear()
    stdscr.refresh()

    screen_height, screen_width = stdscr.getmaxyx()
    win_height = 25
    win_width = 140
    win_start_y = 0
    win_start_x = 0
    win_height = min(win_height, screen_height - 5)
    win_width = min(win_width, screen_width)
    win = curses.newwin(win_height, win_width, win_start_y, win_start_x)
    win.border()

    string_y = 1
    string_x = 1
    win.addstr(string_y, string_x, player.name, curses.color_pair(1))
    #win.addstr(2, 1, player.describe())
    win.refresh()

    msg_win_height = 5
    msg_win_width = win_width
    msg_win_start_y = win_height
    msg_win_start_x = 0

    msg_win = curses.newwin(msg_win_height, msg_win_width, msg_win_start_y, msg_win_start_x)
    msg_win.border()
    msg_win.addstr(1, 1, f"Health: {player.health}")
    msg_win.refresh()

    # Initialize character window variable
    character_win = None

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
        elif key == curses.KEY_RIGHT and string_x < win_width - len(player.name) - 1:
            string_x += 1
        elif key == KEY_CHARACTER:
            # Create a character window
            character_win_height = 10
            character_win_width = 40
            character_win_start_y = (win_height - character_win_height) // 2 + win_start_y
            character_win_start_x = (win_width - character_win_width) // 2 + win_start_x
            stdscr.addstr(screen_height - 1, 0, f"Character Win: {character_win_height}x{character_win_width} at ({character_win_start_y},{character_win_start_x})")  # Debugging line
            stdscr.refresh()
            character_win = curses.newwin(character_win_height, character_win_width, character_win_start_y, character_win_start_x)
            character_win.border()
            character_win.addstr(1, 1, "Character Window")
            character_win.refresh()
        elif key == KEY_CLOSE and character_win is not None:
            # Clear and refresh the main window to remove the character window overlay
            character_win.clear()
            character_win.refresh()
            character_win = None

        # Clear the window and update the string position
        win.clear()
        win.border()
        win.addstr(string_y, string_x, player.name, curses.color_pair(1))
        #win.addstr(2, 1, player.describe())
        win.refresh()

        # Update the message window with the player's health
        msg_win.clear()
        msg_win.border()
        msg_win.addstr(1, 1, f"Health: {player.health}")
        msg_win.refresh()

        if character_win is not None:
            character_win.border()
            character_win.addstr(1, 1, "Character Window")
            character_win.refresh()

# Run the main function using curses.wrapper
curses.wrapper(main)
