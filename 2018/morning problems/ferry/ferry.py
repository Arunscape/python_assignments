# def crossriver(pos,time):
#     if pos=='west':
#         pos='east'
#     elif pos=='east':
#         pos='west'
#     time+=100
#     return (time,pos)
#
# # read the input
# #first line is the times when the vehicles arrive on west bank
# numwest = list(map(int,input().split()))
# numeast = list(map(int,input().split()))
# # solve the problem
# loopw=1
# loope=1
# #want to keep looping as long as there are vehicles
#
# #initial time
# if numwest[0] < numeast[0]:
#     time=numwest[0]
#     pos='west'
#
# elif numwest[0] > numeast[0]:
#     time=numeast[0]
#     pos='east'
#
# while numwest and numeast:
#
#     if numwest[0] < numeast[0]:
#         if pos =='east':
#             time=crossriver(pos,time)[0]
#             pos=crossriver(pos,time)[1]
#         if numwest[0] > time:
#             time=numwest[0]
#         time=crossriver(pos,time)[0]
#         try:
#             del numwest[0]
#         except:
#             #no more vehicles on west side
#             pass
#
#     elif numwest[0] > numeast[0]:
#         if pos =='west':
#             time=crossriver(pos,time)[0]
#             pos=crossriver(pos,time)[1]
#         if numeast[0] > time:
#             time=numwest[0]
#         time=crossriver(pos,time)[0]
#         try:
#             del numeast[0]
#         except:
#             #no more vehicles on east side
#             pass
#     #theoretically should exit loop if either numwest or numeast is 0
#
# while numwest:
#     time=crossriver(pos,time)[0]
#     del numwest[0]
#
# while numeast:
#     time=crossriver(pos,time)[0]
#     del numeast[0]
# print(time)
# # print the answer!
#
# # Hint: consider having a variable tracking the current "time" and
# # a variable tracking which side of the shore the ferry lies on


# numwest = list(map(int,input().split()))
# numeast = list(map(int,input().split()))
#
# print(numwest)
# print(numeast)
# def crossriver():
#
#     global pos
#     global time
#     if pos=='west':
#         pos='east'
#     elif pos=='east':
#         pos='west'
#     time+=100
#
# #initial time
# pos='west'
# time=0
#
# while numwest and numeast:
#
#     try:
#         if numwest[0] < numeast[0] and pos=='west':
#             if numwest[0] > time:
#                 time = numwest[0]
#             crossriver()
#             del numwest[0]
#             continue
#     except:
#         pass
#
#     try:
#         if numwest[0] < numeast[0] and pos=='east':
#             crossriver()
#             if numwest[0] > time:
#                 time = numwest[0]
#
#             crossriver()
#             del numwest[0]
#             continue
#     except:
#         pass
#
#     try:
#         if numeast[0] < numwest[0] and pos=='west':
#             crossriver()
#             if numeast[0] > time:
#                 time = numeast[0]
#             crossriver()
#             del numeast[0]
#             continue
#     except:
#         pass
#
#     try:
#         if numeast[0] < numwest[0] and pos=='east':
#             if numeast[0] > time:
#                 time = numeast[0]
#             crossriver()
#             del numeast[0]
#             continue
#     except:
#         pass
#
#
# while numeast:
#     if pos == 'west':
#         crossriver()
#     if numeast[0] > time:
#         time = numeast[0]
#     crossriver()
#     del numeast[0]
#
# while numwest:
#     if pos == 'east':
#         crossriver()
#     if numwest[0] > time:
#         time = numwest[0]
#     crossriver()
#     del numwest[0]
# print(time)
#
#
#
# print(time)


numwest = list(map(int,input().split()))
numeast = list(map(int,input().split()))

def crossriver():

    global pos
    global time
    if pos=='west':
        pos='east'
    elif pos=='east':
        pos='west'
    time+=100

#initial time
pos='west'
time=0

while numwest and numeast:

    if numwest[0] < numeast[0]:
        #need to move from west side


        #wait for car

        if numwest[0] > time:
            time=numwest[0]

        #if ferry is on the east, move to west
        if pos == 'east':
            crossriver()


        #now the ferry is for sure on the west
        #bring car to other side
        crossriver()

        #get rid of car
        del numwest[0]

    elif numeast[0] < numwest[0]:
        #need to move from west side


        #wait for car

        if numeast[0] > time:
            time=numeast[0]

        #if ferry is on the east, move to east
        if pos == 'west':
            crossriver()


        #now the ferry is for sure on the west
        #bring car to other side
        crossriver()

        #get rid of car
        del numeast[0]

#now, one of the lists is empty. so the ferry should move the cars from one side only

while numwest:
    if numwest[0] > time:
        time=numwest[0]

    #if ferry is on the east, move to west
    if pos == 'east':
        crossriver()


    #now the ferry is for sure on the east
    #bring car to other side
    crossriver()

    #get rid of car
    del numwest[0]

while numeast:
    if numeast[0] > time:
        time=numeast[0]

    #if ferry is on the east, move to east
    if pos == 'west':
        crossriver()


    #now the ferry is for sure on the east
    #bring car to other side
    crossriver()

    #get rid of car
    del numeast[0]
print(time)
