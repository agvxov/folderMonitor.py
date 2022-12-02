#!/bin/python

import sys
import curses

def quit():
	curses.endwin()

def main(agv):
	signal(SIGKILL, quit)
	signal(SIGTERM, quit)
	stdscr = curses.initscr()
	curses.noecho()
	while true:
		folders = []
		os.listdir(".")
		for i in folders:
			stdscr.addstr(i)
		stdscr.refresh()
		sleep 0.5
	

if __name__ == '__main__':
	raise SystemExit(main(sys.argv[1:]))
