"""
DESCRIPTION:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zero(arr):

    zero = arr.count(0)

    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(0)

    for i in range(zero):
        arr.remove(0)

    return arr


print(move_zero([]))