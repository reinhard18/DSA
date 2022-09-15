def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found in list " + index)
    else:
        print("Target not found in list")


ls = [2, 4, 6, 3, 4]
target = 4

a = linear_search(ls, target)
print(a)

verify(ls, target)
