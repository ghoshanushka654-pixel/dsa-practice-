"""
Topic: Sorting and merging linked lists (Module 3)
Problem: Sort a Linked List
Source: LeetCode #148
Difficulty: Medium
Approach: Merge sort is best for lists: find the middle with slow/fast pointers,
          split, sort each half recursively, merge by relinking.
Time: O(n log n)   Space: O(log n) recursion
"""


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def from_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out


def merge(a, b):
    dummy = tail = Node(0)
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next          # slow ends at the END of the first half
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second, slow.next = slow.next, None
    return merge(sort_list(head), sort_list(second))


if __name__ == "__main__":
    assert to_list(sort_list(from_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(sort_list(from_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(sort_list(None)) == []
    print("OK")
