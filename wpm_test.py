import curses
from curses import wrapper

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test")
    stdscr.addstr("\nPress any key to continue")
    stdscr.refresh()
    key = stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello this is some some text for this test"
    current_text = []
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh() 
            
        key  = stdscr.getkey()
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE",'\b','\x7f'):
            
        current_text.append(key)
           

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start(stdscr)
    wpm_test(stdscr)
    
wrapper(main)