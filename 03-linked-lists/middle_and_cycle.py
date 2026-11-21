"""
Topic: Linked list pointer techniques (Module 3)
Problem: (1) Find the middle node  (2) Detect a cycle (Floyd's algorithm)
Source: LeetCode #876, #141
Difficulty: Easy
Approach: Slow pointer moves 1 step, fast pointer moves 2.
          Middle: when fast reaches the end, slow is at the middle.
          Cycle: if there is a cycle, fast eventually meets slow.
Time: O(n)   Space: O(1)
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


def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    assert middle(from_list([1, 2, 3, 4, 5])).data == 3
    assert middle(from_list([1, 2, 3, 4])).data == 3      # second middle
    h = from_list([1, 2, 3, 4])
    assert not has_cycle(h)
    h.next.next.next.next = h.next                        # 4 -> 2 creates a cycle
    assert has_cycle(h)
    print("OK")
