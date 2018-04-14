h = list(map(int, input().split()))
out = list()
max = float('-inf')
midx = 0

# for i in range(len(h)):
#     try:
#         if h[i - 1] > h[i]:
#             out.append(i - 1)
#
#         elif h[i] > h[max]:
#             max = i
#             out.append('X')
#
#         else:
#             idx = i - 1
#             while h[idx] < h[i]:
#                 idx = out[idx]
#             out.append(idx)
#
#     except IndexError:
#         continue
# catch on first loop when it tries to index i-1 but i=0

for i in range(len(h)):
    try:

        if h[i] > max:
            max, midx = h[i], i
            out.append('X')
        elif h[i - 1] > h[i]:
            out.append(i - 1)
        else:
            idx = i - 1
            while h[idx] < h[i]:
                idx = out[idx]
            out.append(idx)
    except IndexError:
        continue
        # catch on first loop when it tries to index i-1 but i=0
print(*out)
