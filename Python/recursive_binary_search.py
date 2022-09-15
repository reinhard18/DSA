def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # Stopping condition
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


ls = [2, 1, 6, 3, 4]
target = 4


def verify(result):
    print("Target found ", result)


result = recursive_binary_search(ls, target)
verify(result)
