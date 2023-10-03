from collections import deque

exp = input().split()
numbers = deque()

for char in exp:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            num1 = numbers.popleft()
            num2 = numbers.popleft()
            if char == '+':
                numbers.appendleft(num1 + num2)
            elif char == '-':
                numbers.appendleft(num1 - num2)
            elif char == '*':
                numbers.appendleft(num1 * num2)
            elif char == '/':
                numbers.appendleft(num1 // num2)

print(numbers[0])


"""71/100"""
# from collections import deque
# from math import floor
#
# string = input().split()
# operators = '*+-/'
# result = 0
# current_numbers = deque([])
# FLAG = False
#
# for char in string:
#     # if char.isnumeric():
#     #     current_numbers.append(int(char))
#     if char[0] == '-' and char[1:].isnumeric():
#         current_numbers.append(int(char))
#     elif char.isnumeric():
#         current_numbers.append(int(char))
#     elif char in operators:
#         if not FLAG:
#             FLAG = True
#             if len(current_numbers) == 2:
#                 num1 = current_numbers.popleft()
#                 num2 = current_numbers.popleft()
#                 if char == '*':
#                     result = num1 * num2
#                 elif char == '+':
#                     result = num1 + num2
#                 elif char == '-':
#                     result = num1 - num2
#                 elif char == '/':
#                     result = floor(num1 / num2)
#             else:
#                 num1 = current_numbers.popleft()
#                 if char == '*':
#                     result = num1
#                 elif char == '+':
#                     result = num1
#                 elif char == '-':
#                     result = num1
#                 elif char == '/':
#                     result = num1
#         else:
#             if len(current_numbers) == 2:
#                 num1 = current_numbers.popleft()
#                 num2 = current_numbers.popleft()
#                 if char == '*':
#                     result = result * num1 * num2
#                 elif char == '+':
#                     result = result + num1 + num2
#                 elif char == '-':
#                     result = result - num1 - num2
#                 elif char == '/':
#                     result = floor(result / num1 / num2)
#             else:
#                 num1 = current_numbers.popleft()
#                 if char == '*':
#                     result = result * num1
#                 elif char == '+':
#                     result = result + num1
#                 elif char == '-':
#                     result = result - num1
#                 elif char == '/':
#                     result = floor(result / num1)
#
# print(result)





"""
wrong requirements understanding
"""
# string = input().split()
# checker = string.copy()
# result = 0
# operators = '*+-/'
# numbers = ''
# operator_save = ''
# HAD_OPERATOR = False
#
# for char in string:
#     if char.isdigit:
#         numbers += char
#
#     elif char in operators:
#         numbers = int(numbers)
#         if not HAD_OPERATOR:
#             operator_save = char
#             HAD_OPERATOR = True
#             result = numbers
#             numbers = ''
#             continue
#         if operator_save == '*':
#             result *= numbers
#             numbers = ''
#         elif operator_save == '+':
#             result += numbers
#             numbers = ''
#         elif operator_save == '-':
#             result -= numbers
#             numbers = ''
#         elif operator_save == '/':
#             result /= numbers
#             numbers = ''
#         operator_save = char
#