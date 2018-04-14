_ = input()
li = list(map(int, input().split() ))

maxi , cur = 0,0

for i in li:
    cur = max(cur+i,0)
    maxi = max(cur, maxi)

print(maxi)
