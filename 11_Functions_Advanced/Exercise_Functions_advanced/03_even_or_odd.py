def even_odd(*args):
    command = args[-1]
    resulting_list = []
    if command == 'even':
        for num in args:
            try:
                num % 2 == 0
            except TypeError:
                break
            if num % 2 == 0:
                resulting_list.append(num)

    elif command == 'odd':
        for num in args:
            try:
                num % 2 != 0
            except TypeError:
                break
            if num % 2 != 0:
                resulting_list.append(num)
    return resulting_list


"""
test prints
"""
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
