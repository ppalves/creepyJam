import time
import curses
import os

# writes a string to a window with delay between chars
def textStream(text, window):
    for c in text:
        curses.napms(200)
        window.addch(c)
        window.refresh()
    window.addch("\n")
    window.move(window.getyx()[0],2)
    window.border()
    window.refresh()


def main(stdscr):
    # Clear screen
    stdscr.clear()
    # change directory
    os.chdir("../assets")
    # display art
    with open('asciiArt.txt', 'r') as art:
        i=0
        for line in art:
            stdscr.addstr(i+5, int(curses.COLS/2)-35, line) 
            i+=1
    stdscr.border()
    stdscr.refresh()
    
    # text window
    win = stdscr.subwin(int((curses.LINES-1)/3), curses.COLS-2, int(2*(curses.LINES-1)/3), 1)
    win.border()
    win.refresh()
    win.move(2, 2)
    textStream("Hi jeff", win)
    textStream("It's me the Dean", win)

    # waits for keyboard
    stdscr.getkey()

curses.wrapper(main)


#if __name__=="__main__":
#    main()
