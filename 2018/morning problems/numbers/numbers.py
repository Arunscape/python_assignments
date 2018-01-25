# NOTE: you should figure out how to read the input for this problem yourself
# as it is good practice for real morning problems.

# read number of friends
numfriends=int(input())
# for each friend, read their numbers..
fdict={}
for i in range(numfriends):
# read the index of friend whose numbers should be printed
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    numbers.pop(0)
    fdict[i]=numbers
# print the favourite numbers of the selected friend
getthisnum = int(input())
print(fdict[getthisnum])
