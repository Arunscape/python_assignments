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
"""

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    from exercise6 import *
    # print(findValley([10, 7, 4, 1, 3, 6]))
    # print(findValley([3, 2, 1]))
    # print(findValley([9, 14]))
    # print(findValley([5, 6, 1, 2, 3, 4]))
    print( climbing([30, 70, 95, 120, 145, 190], 10, 210) )
    # print(climbing([50, 100], 1, 100))
    # print(climbing([50, 99], 1, 100))
