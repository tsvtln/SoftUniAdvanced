def print_alphabetic_error():
    print("First value must be an alphabetic entry.")


numbers_dictionary, line = {}, ''

# Search module
while line != "Search":
    line = input()
    if line == 'Search':
        continue
    if line.isalpha():
        try:
            numbers_dictionary[line] = int(input())
        except ValueError:
            print('The variable number must be an integer')
    else:
        print_alphabetic_error()

# Remove module
while line != "Remove":
    line = input()
    if line == 'Remove':
        continue
    if not line.isalpha():
        print_alphabetic_error()
        continue
    elif line in numbers_dictionary.keys():
        print(numbers_dictionary[line])
    else:
        print("Value not found.")

# End module
while line != "End":
    line = input()
    if line == 'End':
        continue
    if not line.isalpha():
        print_alphabetic_error()
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
