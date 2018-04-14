words = input().split()

d=dict()
# words is now a list of all strings in the input
for word in words:
    if word not in d:
        d[word]=1
    elif word in d:
        d[word]+=1

# maxval=max(d, key=lambda i: d[i])
# maxval=max(int(k) for k in d)
# # maxval=max(d)
# # print(maxval)
# maxlist=list()
max_value = max(d.values())
max_list = [k for k, v in d.items() if v == max_value]
# for key, val in d.items():
#     if val == maxval:
#         maxlist.append(key)
# print(maxlist)
for x in sorted(max_list):
    print(x)
# # finish the problem!
# print(d)
#print(d)
