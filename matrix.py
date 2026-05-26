#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)

    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    max_y, max_x = stdscr.getmaxyx()
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワ"

    cols = [[random.randint(-max_y, 0), random.randint(1, 3)] for _ in range(max_x)]

    while True:
        stdscr.erase()
        for x in range(max_x):
            y, speed = cols[x]
            for i in range(speed * 3):
                draw_y = y - i
                if 0 <= draw_y < max_y:
                    ch = random.choice(chars)
                    if i == 0:
                        stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                    elif i < speed * 2:
                        stdscr.attron(curses.color_pair(2))
                    else:
                        stdscr.attron(curses.color_pair(2) | curses.A_DIM)
                    try:
                        stdscr.addch(draw_y, x, ch)
                    except curses.error:
                        pass
                    stdscr.attroff(curses.A_BOLD | curses.A_DIM)

            cols[x][0] += speed
            if cols[x][0] >= max_y + speed * 3:
                cols[x] = [random.randint(-10, -1), random.randint(1, 3)]

        try:
            key = stdscr.getch()
            if key == ord('q'):
                break
        except curses.error:
            pass

        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)
