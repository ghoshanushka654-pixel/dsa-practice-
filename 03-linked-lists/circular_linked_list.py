"""
Topic: Circular linked lists (Module 3, high priority)
Problem: Circular singly linked list with a tail pointer, plus the Josephus problem.
Source: Classic / GeeksforGeeks
Difficulty: Medium
Approach: Keep `tail`; tail.next is the head, so insert at BOTH ends is O(1).
          Traverse until you come back to the tail (never loop forever).
Time: front/end insert O(1), traversal O(n)   Space: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert_front(self, x):
        n = Node(x)
        if not self.tail:
            n.next = n
            self.tail = n
        else:
            n.next = self.tail.next
            self.tail.next = n

    def insert_end(self, x):
        self.insert_front(x)
        self.tail = self.tail.next

    def delete_front(self):
        if not self.tail:
            raise IndexError("underflow")
        head = self.tail.next
        if head is self.tail:
            self.tail = None
        else:
            self.tail.next = head.next
        return head.data

    def to_list(self):
        if not self.tail:
            return []
        out, cur = [], self.tail.next
        while True:
            out.append(cur.data)
            if cur is self.tail:
                break
            cur = cur.next
        return out


def josephus(n, k):
    """n people in a circle, every k-th is eliminated. Returns the survivor (1-indexed)."""
    people, idx = list(range(1, n + 1)), 0
    while len(people) > 1:
        idx = (idx + k - 1) % len(people)
        people.pop(idx)
    return people[0]


if __name__ == "__main__":
    c = CircularLinkedList()
    c.insert_end(2); c.insert_end(3); c.insert_front(1)
    assert c.to_list() == [1, 2, 3]
    assert c.delete_front() == 1 and c.to_list() == [2, 3]
    assert josephus(7, 3) == 4
    print("OK")
