from os import link
from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublist containing a single node
    - Repeatedly merge the sublist to produce sorted sublists until one remain

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size: linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return right_half, left_half


def merge(left, right):
    """
    Merge  two linked lists, sorting by data in nodes
    Returns a new , merge list
    """

    # Create  a new linked list  that contains node from merging right and left

    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for head and right head linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from right to merged linked list

        if left_head is None:
            current.next_node = right_head
            # Call next  on right  to set loop condition to False
            right_head = right_head.next_node
        # if the head node  of right is none, we're past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next  on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data
