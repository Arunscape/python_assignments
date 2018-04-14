n = int(input())

#flights=list()
flights=dict()
# n is the number of flights available
for i in range(n):
    start, end = input().split("---")
    # now we have the two strings for each of the first n lines
    # do something with them!
    #flights.append([start,end])
    flights[start]=end

q = int(input())
#q is the number of queries
#print(q)
for i in range(q):
    startcity = input().strip()
    #print('this is the start city: {}'.format(startcity))
    #x=''
    cnt=0
    # if startcity=='Edmonton':
    #     break
    while startcity != "Edmonton":
        startcity=flights[startcity]
        # print('this is the next city: {}'.format(x))
        cnt += 1
    print(cnt)
    # x=flights[startcity]
    # print('this is the next city: {}'.format(x))

# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines

# for each query, calculate and print the answer
