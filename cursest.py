#   A simple program which counts the number of columns 
#   and rows available on the terminal screen
#   03/05/2013

import curses  # Import the curses module
import time

stdscr = curses.initscr()  # Initialize the main window 
curses.noecho()  # Disable immediate output from keyboard to screen
curses.cbreak()  # <Enter> key not required to submit keypresses
curses.curs_set(0)  # Renders cursor invisible (1 = underline, 2 = block)
stdscr.keypad(1)  # Accept special names from navigation keys (arrow keys, home, etc.)

yx = stdscr.getmaxyx()  # Get maximum cursor positions in y and x

# Count number of available columns of screen
stdscr.erase()  
for i in range(yx[1]):
  stdscr.addstr(0,i,"^")
	for c in range(len(str(i))):
		stdscr.addstr(1+c,i,str(i+1)[c])
	stdscr.refresh()
	time.sleep(0.02)

m = "Column count complete! %d columns available." % yx[1]
stdscr.addstr(yx[0]/2, (yx[1]-len(m))/2, m, curses.A_BOLD)  # Print text centered in screen
stdscr.refresh()
time.sleep(3)

# Count number of available rows on screen
stdscr.erase()
for i in range(yx[0]):
	stdscr.addstr(i,0,"< "+str(i+1)) 
	stdscr.refresh()  # Refresh sceen to reflect new text
	time.sleep(0.05)  # Sleep briefly between updates

m = "Row count complete! %d rows available." % yx[0]
stdscr.addstr(yx[0]/2,(yx[1]-len(m))/2, m, curses.A_BOLD)
stdscr.refresh()
time.sleep(3)

# Reverse changes before returning to Terminal mode
stdscr.erase()
stdscr.refresh()
stdscr.move(0,0)
curses.echo()
curses.nocbreak()
stdscr.keypad(0)
curses.endwin()

