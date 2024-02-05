def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

#
# def find_largest_int(arr):
#     largest = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#     return largest