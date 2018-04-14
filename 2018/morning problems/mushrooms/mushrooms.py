# import numpy as np
# crit = int(input())
# mushrooms = np.array(list(map(int,input().split())))
#
# out = list()
#
# curr =0
# for i in range(len(mushrooms)):
#     #i is the current spot
#     #cnt is the thing to append
#     #temp is the num of mushrooms picked at that spot onwards
#     temp=0
#     cnt=0
#     spot=i
#     j=0 #offset
#
#     try:
#         while temp < crit: #and spot+j< len(mushrooms):
#             temp += mushrooms[spot+j]
#             cnt += 1
#             j+=1
#             # print(temp, spot+j)
#         out.append(cnt)
#     except IndexError:
#         out.append(0)
#
#
#     #i++
# if crit == 0:
#     print(*[1]*len(mushrooms))
# else:
#     print(*out)
#NOOOO IT'S TOO SLOW


# crit = int(input())
# mushrooms = list(map(int,input().split()))
#
# if crit == 0:
#     print(*[1]*len(mushrooms))
#
# else:
#     out = list()
#     lo = hi = cnt = 0
#     temp=mushrooms[0] #initial mushrooms
#
#     while lo < len(mushrooms)-1:
#
#         try:
#
#             if temp < crit and hi != len(mushrooms)-1:
#                 hi+=1
#                 temp += mushrooms[hi]
#
#             elif temp < crit and hi == len(mushrooms)-1:
#                 out[lo]=0
#                 lo+=1
#
#             #at the end
#             elif temp >= crit:
#                 #should only subtract this if we reach the crit count
#
#                 temp -= mushrooms[lo] #before moving window, subract mushrooms[lo] form temp
#                 lo += 1
#                 # out.append(cnt)
#
#
#         except IndexError:
#             out.append(0)
#
#
#     print(*out)


crit = int(input())
mushrooms = list(map(int,input().split()))

if crit == 0:
    print(*[1]*len(mushrooms))

else:
    out = list()
    lo = hi = cnt = 0
    temp=mushrooms[0] #initial mushrooms

    while lo < len(mushrooms)-1:

        try:
            # print(lo,hi,temp)
            if temp < crit:
                hi+=1
                temp += mushrooms[hi]
                cnt+=1

            #at the end
            elif temp >= crit:
                #should only subtract this if we reach the crit count

                temp -= mushrooms[lo] #before moving window, subract mushrooms[lo] form temp
                out.append(hi-lo+1)
                lo += 1

                # print('\n')


        except IndexError:
            # out.append(0)
            # lo+=1
            # hi=lo
            # temp=0
            # break
            out += [0]*(len(mushrooms)-lo)
            break

    if len(out) == len(mushrooms)-1:
        if mushrooms[-1] >= crit:
            out.append(1)
        else:
            out.append(0)
    print(*out)
