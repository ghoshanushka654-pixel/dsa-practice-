"""
Topic: Sorting and merging linked lists (Module 3)
Problem: Merge Two Sorted Lists
Source: LeetCode #21
Difficulty: Easy
Approach: Compare the two heads, attach the smaller to the result tail and advance;
          finally attach whatever remains. Relink nodes, do not copy them.
Time: O(m+n)   Space: O(1) extra
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


if __name__ == "__main__":
    assert to_list(merge(from_list([1, 3, 5]), from_list([2, 4, 6, 8]))) == [1, 2, 3, 4, 5, 6, 8]
    assert to_list(merge(None, from_list([1]))) == [1]
    assert to_list(merge(None, None)) == []
    print("OK")
