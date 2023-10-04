string = input().split('|')
mx = []

for i in range(len(string) - 1, -1, -1):
    row = [int(x) for x in string[i].split()]
    if row:
        mx.append(row)
for row in mx:
    print(*row, sep=' ', end=' ')



# import re
#
# string = input().split()
# lst = []
# tmp_lst = []
# long = 0
# #
# # for char in string:
# #     if '|' in char:
# #         long += 1
#
# # for i in range(long):
# for char in string:
#     if '|' in char:
#         if re.findall(r'\d+\.\d+|\d+', char):
#             num = re.findall(r'\d+\.\d+|\d+', char)
#             lst.append(tmp_lst)
#             tmp_lst = []
#             tmp_lst.append(num)
#         else:
#             lst.append(tmp_lst)
#             tmp_lst = []
#
#     elif char.isdigit():
#         tmp_lst.append(char)
#
# print(lst)
