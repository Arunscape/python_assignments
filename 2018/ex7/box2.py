'''
Arun Woosaree
-------------------------------------------------------------------------------
>>> boxes = [Box(0, 0, 10, 10), Box(1, 1, 8, 8), Box(2, 2, 6, 6), Box(3, 3, 4, 4)]
>>> longest_sequence(boxes, 0)
4
'''
# You will need to implement the function longest_sequence as appears in box2.py
# which can be download from the link below. See the file for a full description
# of the task.  Do not change the declaration of the longest_sequence function.
# You may add helper functions to the same file if you think it will help. For
# full marks, your implementation should run in O(n2) time. Also, regardless of
# the running time you achieve, a small part of the marks is allocated to
# running time analysis. At the bottom of box2.py, you will see a comment
# prompting you to briefly analyze the running time. You should put a statement
# of the running time plus a brief justification (2-3 sentences) in a comment at
# the bottom of your code.


class Box:
    def __init__(self, x, y, w, h):
        '''
        Create an instance of the box class whose lower-left corner is at (x,y)
        and whose width is w and height is h. The width w and height h must be
        positive.
        '''

        if w <= 0 or h <= 0:
            raise ValueError("cannot create box with nonpositive dimensions")
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def moveBy(self, dx, dy):
        '''
        Translates this box by dx units along the x axis and dy units along
        the y axis.
        '''
        self.x += dx
        self.y += dy

    def contains(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns true if and only if the box b is entirely contained
        within this box (they can share edges).
        '''
        return (self.x <= b.x and self.y <= b.y and
                self.x + self.w >= b.x + b.w and
                self.y + self.h >= b.y + b.h)

    def unionWith(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns the smallest box that contains both self and box b.
        '''
        new_x = min(self.x, b.x)
        new_y = min(self.y, b.y)
        new_w = max(self.x + self.w, b.x + b.w) - new_x
        new_h = max(self.y + self.h, b.y + b.h) - new_y
        return Box(new_x, new_y, new_w, new_h)

    def __str__(self):
        return "Box({}, {}, {}, {})".format(self.x, self.y,
                                            self.w, self.h)


def longest_sequence(boxes, i, memo=None):
    '''
    Assumes boxes is a list of boxes indexed by i ( 0  <= i < len(boxes) )
    and that no two boxes have identical (x, y, w, h),
    i.e., no two boxes are the same.

    This function returns the largest value m such that
    it is possible to find a list of length m of distinct boxes starting at boxes[i]
    where each box in the list contains the next box in the list
    (according to the contains() method).

    Note, the boxes in "chain" don't have to be in the same order
    as they appeared in the boxes list.

    Example:
    boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    longest_sequence(boxes, 1) returns 2

    boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    longest_sequence(boxes2, 1) returns 3

    For full marks, your algorithm should run in O(n^2) time where
    n = len(boxes). Use dynamic programming (top-down approach)
    to achieve this.

    DOCTESTS:
    --------------------------------------------------------------------
    >>> boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    >>> longest_sequence(boxes, 1)
    2

    >>> boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    >>> longest_sequence(boxes2, 1)
    3
    '''
    # print(memo)
    # now you finish it
    if memo is None:
        memo = {}
        # memo dict is in the following format:
        # key: value
        #    i:what this function should return for given i

    if i in memo:
        return memo[i]
        # yay we're done

    # if box contains other box which contains more boxes, add to memo
    currentlongest = 1
    currentsequence = 1
    for idx, b in enumerate(boxes):

        # this little and below is what prevents maximum recursion depth,
        # because the contains() method is defined such that a box can contain
        # itself, so this would just keep recursing until max depth was reached
        if boxes[i].contains(b) and boxes[i] != b:
            # print(longest_sequence(boxes, idx, memo))
            currentsequence += longest_sequence(boxes, idx, memo)
            if currentsequence > currentlongest:
                # new longest, update memo
                memo[i] = currentlongest = currentsequence
                # reset count because we are going to try another sequence now
                currentsequence = 1
    return currentlongest


# ADD COMMENT BELOW TO ANALYZE THE RUNNING TIME
# State the running time of your algorithm below here. Justify it in 2-3
# sentences. Remember the "running time analysis template"
# for dynamic programming problems from the lectures.
#####################################################
# # Running Time Analysis Template
# # Running time = (# of distinct subproblems we need to solve)
# # multiplied by
# # (computation required to solve each subproblem) + (computation
# # required to combine solutions to solve the original problem, this is
# # outside the function that is called recursively)
'''
We have an input of n boxes.

main problem: find the longest sequence
    the main for loop runs n times

the subproblem:
    find the max longest sequence of the sequences available from the boxes stored in boxes[i]
    i.e. for the boxes in boxes[i], find the box with the longest sequence

    to solve each subproblem, the loop runs n times as well, and memoization
    saves re-computing already calculated subproblems

so the main problem runs n times, and each subproblem runs n times as well

so, O(n*n) = O(n^2)


'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    # print(longest_sequence(boxes, 1))  # returns 2
    #
    # boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    # print(longest_sequence(boxes2, 1))  # returns 3
    #
    # boxes = [Box(0, 0, 10, 10), Box(1, 1, 8, 8),
    #          Box(2, 2, 6, 6), Box(3, 3, 4, 4)]
    # print(longest_sequence(boxes, 0))  # should return 4
