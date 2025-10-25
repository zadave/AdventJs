import re


def is_robot_back(moves):
    x, y = 0, 0
    seen = {}
    dir_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    inv_map = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

    tokens = re.findall(r'([*!?]?[LRUD])', moves)
    for token in tokens:
        if len(token) > 1:
            m, c = token[0], token[1]
        else:
            m, c = '', token

        if m == '!':
            c = inv_map[c]
        dx, dy = dir_map[c]
        if m == '*':
            dx, dy = dx * 2, dy * 2
        if m == '?' and seen.get(c):
            continue

        x += dx
        y += dy
        seen[c] = True

    return True if x == 0 and y == 0 else (x, y)
