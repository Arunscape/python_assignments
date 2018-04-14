# n = int(input())
#
# busses = sorted(list(map(int, input().split())))
#
# try:
#     for i in range(n-2):
#         currentbus = busses[i]
#         nextbus=busses[i+1]
#         nextnextbus=busses[i+2]
#
#         # print(currentbus, nextbus-1,)
#         if currentbus == nextbus - 1 and currentbus == nextnextbus-2:
#             del busses[i+1]
#             # del busses[i+2]
#             busses[i]= '{}-{}'.format(currentbus, nextnextbus)
#
#     for i in range(len(busses)):
#         try:
#             # print(busses[i].split('-')[1])
#             if int(busses[i].split('-')[1]) == busses[i+1]:
#                 del busses[i+1]
#         except AttributeError:
#             pass
#
#     for i in range(len(busses)):
#         try:
#             if int(busses[i].split('-')[1]) == int(busses[i+1].split('-')[0]):
#                 busses[i] = '{}{}'.format(busses[i].split('-')[0],busses[i+1].split('-')[1])
#             elif False:
#                 pass
#         except AttributeError:
#             pass
# print(busses)

n = int(input())
busses = sorted(list(map(int, input().split())))

# from numpy import array, diff, where, split


# grouped = list()
# pre, temp = busses[0], [busses[0]]
#
# for num in busses[1:]:
#     if pre < num-2:
#         grouped += [temp]
#         temp = [num]
#     else: temp.append(num)
#
#     pre=num
# grouped.append(temp)
#
# # print(*grouped)
# out=list()
# for l in grouped:
#     if len(l) ==1: out.append(l[0])
#     elif len(l) ==2: out += [l[0], l[1]]
#     else: out.append('{}-{}'.format(l[0],l[-1]))
# print(*out)

import numpy as np
grouped =np.split(busses, np.where(np.diff(busses) != 1)[0]+1)
out = list()
for l in grouped:
    if len(l) ==1: out.append(l[0])
    elif len(l) ==2: out += [l[0], l[1]]
    else: out.append('{}-{}'.format(l[0],l[-1]))

print(*out)
