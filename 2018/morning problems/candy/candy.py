n = int(input())

candy = list(map(int,input().split()))

cansum = sum(candy)
samesize = cansum/2

import itertools
combo= [c for i in range(0,n) for c in itertools.combinations(candy, i) if sum(c) == samesize]

# print(combo)

# if not samesize.is_integer(): print(False)
if combo: print(True)
else: print(False)
