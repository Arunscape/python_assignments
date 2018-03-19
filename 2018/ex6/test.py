"""
>>> from exercise6 import *
>>> findValley([10, 7, 4, 1, 3, 6])
3

>>> findValley([4])
0
>>> findValley([3, 2, 1])
2
>>> findValley([9, 14])
0
>>> findValley([11, 2, 11, 12])
1
>>> findValley([6, 5, 1, 2, 3, 4])
2
>>> findValley([1, 2, 3, 4])
0
>>> findValley([1])
0
>>> findValley([1, 2])
0
>>> findValley([2, 1])
1
>>> findValley([7, 6, 5, 1, 2, 3, 4])
3
>>> findValley([1, 2, 3, 4, 5, 6, 7])
0
>>>
>>>
>>>
>>> climbing([30, 70, 95, 120, 145, 190], 10, 210)
70
>>> climbing([50, 100], 1, 100)
100
>>> climbing([50, 99], 1, 100)
50
>>> climbing([1,2,3,4,5,6,7,8,9,10], 10, 100)
2
>>> climbing([35, 77, 92, 103, 107, 115, 123, 124, 142, 153, 155, 163, 167,174, 180, 189, 190, 196, 201, 205, 208, 220, 226, 244, 247, 250, 254, 259, 273,274, 286, 297, 311, 312, 322, 323, 326, 329, 352, 376, 379, 385, 402, 407, 418,420, 428, 453, 459, 460, 499, 501, 504, 506, 509, 524, 532, 535, 537, 561, 567,579, 590, 597, 600, 611, 616, 643, 647, 672, 686, 692, 705, 711, 720, 724, 749,753, 773, 775, 776, 795, 802, 818, 819, 823, 827, 832, 839, 840, 850, 859, 874,880, 889, 910, 921, 947, 948, 958], 21, 9001)
35
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # from exercise6 import *
    # print(findValley([10, 7, 4, 1, 3, 6]))
    # print(findValley([3, 2, 1]))
    # print(findValley([9, 14]))
    # print(findValley([5, 6, 1, 2, 3, 4]))
    # print( climbing([30, 70, 95, 120, 145, 190], 10, 210) )
    # print(climbing([50, 100], 1, 100))
    # print(climbing([50, 99], 1, 100))
#     print(climbing([35, 77, 92, 103, 107, 115, 123, 124, 142, 153, 155, 163, 167,
# 174, 180, 189, 190, 196, 201, 205, 208, 220, 226, 244, 247, 250, 254, 259, 273,
# 274, 286, 297, 311, 312, 322, 323, 326, 329, 352, 376, 379, 385, 402, 407, 418,
# 420, 428, 453, 459, 460, 499, 501, 504, 506, 509, 524, 532, 535, 537, 561, 567,
# 579, 590, 597, 600, 611, 616, 643, 647, 672, 686, 692, 705, 711, 720, 724, 749,
# 753, 773, 775, 776, 795, 802, 818, 819, 823, 827, 832, 839, 840, 850, 859, 874,
# 880, 889, 910, 921, 947, 948, 958], 21, 9001))
