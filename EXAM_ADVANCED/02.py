mx_size = int(input())
temp_list, command = [], ''
tmp_r, tmp_c, collected_fish = 0, 0, 0
WHIRLPOOL = False

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
mx = [list(input()) for _ in range(mx_size)]
ship_location = next(((r, find_ship.index('S')) for r, find_ship in enumerate(mx) if 'S' in find_ship), None)


def move_ship(sl, gsl):
    mx[sl[0]][sl[1]] = '-'
    mx[gsl[0]][gsl[1]] = 'S'
    global ship_location
    ship_location = (gsl[0], gsl[1])


def whirlpool():
    global WHIRLPOOL, collected_fish
    WHIRLPOOL, collected_fish = True, 0


for command in iter(input, "collect the nets"):
    row_advance, col_advance = directions[command][0], directions[command][1]

    if command == 'up':
        if ship_location[0] - (-row_advance) < 0:
            row_advance = mx_size - 1
        else:
            row_advance = ship_location[0] - (-row_advance)
        get_symbol, get_symbol_location = mx[row_advance][ship_location[1]], (row_advance, ship_location[1])
        if get_symbol == '-':
            move_ship(ship_location, get_symbol_location)
        elif get_symbol.isdigit():
            collected_fish += int(get_symbol)
            move_ship(ship_location, get_symbol_location)
        elif get_symbol == 'W':
            whirlpool()
            move_ship(ship_location, get_symbol_location)
            break

    elif command == 'down':
        if ship_location[0] + row_advance > mx_size - 1:
            row_advance = 0
        else:
            row_advance = ship_location[0] + row_advance
        get_symbol, get_symbol_location = mx[row_advance][ship_location[1]], (row_advance, ship_location[1])
        if get_symbol == '-':
            move_ship(ship_location, get_symbol_location)
        elif get_symbol.isdigit():
            collected_fish += int(get_symbol)
            move_ship(ship_location, get_symbol_location)
        elif get_symbol == 'W':
            whirlpool()
            move_ship(ship_location, get_symbol_location)
            break

    elif command == 'left':
        if ship_location[1] - (-col_advance) < 0:
            col_advance = mx_size - 1
        else:
            col_advance = ship_location[1] - (-col_advance)
        get_symbol, get_symbol_location = mx[ship_location[0]][col_advance], (ship_location[0], col_advance)
        if get_symbol == '-':
            move_ship(ship_location, get_symbol_location)
        elif get_symbol.isdigit():
            collected_fish += int(get_symbol)
            move_ship(ship_location, get_symbol_location)
        elif get_symbol == 'W':
            whirlpool()
            move_ship(ship_location, get_symbol_location)
            break

    elif command == 'right':
        if ship_location[1] + col_advance > mx_size - 1:
            col_advance = 0
        else:
            col_advance = ship_location[1] + col_advance
        get_symbol, get_symbol_location = mx[ship_location[0]][col_advance], (ship_location[0], col_advance)
        if get_symbol == '-':
            move_ship(ship_location, get_symbol_location)
        elif get_symbol.isdigit():
            collected_fish += int(get_symbol)
            move_ship(ship_location, get_symbol_location)
        elif get_symbol == 'W':
            whirlpool()
            move_ship(ship_location, get_symbol_location)
            break

print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
      f"Last coordinates of the ship: [{ship_location[0]},{ship_location[1]}]") if WHIRLPOOL else \
    (print("Success! You managed to reach the quota!") if collected_fish >= 20 else
     print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} "
           f"tons of fish more."))
print(f"Amount of fish caught: {collected_fish} tons.") if collected_fish > 0 else None
[print(''.join(line)) for line in mx] if not WHIRLPOOL else None
