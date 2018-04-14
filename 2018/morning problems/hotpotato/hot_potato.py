# a queue may be helpful, but is not necessary
from collections import deque

# read the Inputs
n,q = list(map(int,input().split()))
# solve the problem

# l = list(range(n))
# l[0]='P'

current=0

# print(list(range(n-1)))

# for i in range(n-1):
#     # current += q% len(l)
#     # current = current % len(l)
#     current=q%n
#     while l[current] =='\\':
#         current = (current+1)%n
#     # current =q%n
#     l[current] = '\\'
#     current = (current+1)%n
#     print(i,current,l)

# person=0
# for i in range(n-1):
#     person = (person + q +1) % len(l)
#     l= l[:current]+l[current+1:]
#     print(person,l)
# # print the answer

# players=deque(n)
# players.popleft
# passes=q
#
# while len(players != 1):
#     for _ in range(passes-1):
#         players.extend(players[0])
#         players.popleft()
#     players.popleft
d= deque(range(n))
d.rotate(-1)
while len(d)>1:
    d.rotate(-(q-1))
    d.popleft()
print(d.pop())
# Be mindful of running time, deleting an item in the middle of a list is
# too expensive! The intended running time is O(n*q).

# If the test center is taking forever, press ctrl-c from the terminal
# where you launched the test center to quit it prematurely.
