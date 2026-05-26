#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)

    curses.start_color()
    curses.use_default_colors()

    # color pairs: lead (bold), body (normal), trail (dim)
    colors = [
        (curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_GREEN),
        (curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_RED),
        (curses.COLOR_CYAN, curses.COLOR_CYAN, curses.COLOR_CYAN),
        (curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_YELLOW),
        (curses.COLOR_MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA),
        (curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLUE),
        (curses.COLOR_WHITE, curses.COLOR_WHITE, curses.COLOR_WHITE),
    ]

    for i, (lead, body, trail) in enumerate(colors, 1):
        base = (i - 1) * 3
        curses.init_pair(base + 1, lead, -1)
        curses.init_pair(base + 2, body, -1)
        curses.init_pair(base + 3, trail, -1)

    max_y, max_x = stdscr.getmaxyx()
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワ"

    # each column: [y, speed, color_index]
    cols = [[random.randint(-max_y, 0),
             random.randint(1, 3),
             random.randrange(len(colors))] for _ in range(max_x)]

    while True:
        stdscr.erase()
        for x in range(max_x):
            y, speed, ci = cols[x]
            base = ci * 3
            for i in range(speed * 4):
                draw_y = y - i
                if 0 <= draw_y < max_y:
                    ch = random.choice(chars)
                    if i == 0:
                        pair = curses.color_pair(base + 1) | curses.A_BOLD
                    elif i < speed * 2:
                        pair = curses.color_pair(base + 2)
                    elif i < speed * 3:
                        pair = curses.color_pair(base + 2) | curses.A_DIM
                    else:
                        pair = curses.color_pair(base + 3) | curses.A_DIM
                    stdscr.attron(pair)
                    try:
                        stdscr.addch(draw_y, x, ch)
                    except curses.error:
                        pass
                    stdscr.attroff(pair)

            cols[x][0] += speed
            if cols[x][0] >= max_y + speed * 4:
                cols[x] = [random.randint(-10, -1),
             random.randint(1, 2),
                           random.randrange(len(colors))]

        try:
            key = stdscr.getch()
            if key == ord('q'):
                break
        except curses.error:
            pass

        time.sleep(0.08)

if __name__ == "__main__":
    curses.wrapper(main)
