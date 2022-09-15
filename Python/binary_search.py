def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


def verify(index):
    if index is not None:
        print("Target found in list ", index)
    else:
        print("Target not found in list")


ls = [2, 1, 6, 3, 4]
target = 4

result = binary_search(ls, target)
verify(target)
