"""
Topic: Singly linked lists (Module 3, high priority)
Problem: Implement insert (front / middle / end), delete (front / middle / end),
         search and reverse on a singly linked list.
Source: Classic
Difficulty: Easy-Medium
Approach: Node = data + next.
          insert after p: new.next = p.next; p.next = new   (ORDER MATTERS)
          delete middle:  prev.next = cur.next
Time: front O(1); end O(n) without a tail pointer; search/delete O(n)   Space: O(1)
"""


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, x):
        self.head = Node(x, self.head)

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def insert_after(self, key, x):
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        if cur is None:
            return False
        cur.next = Node(x, cur.next)
        return True

    def delete_front(self):
        if not self.head:
            raise IndexError("underflow")
        v = self.head.data
        self.head = self.head.next
        return v

    def delete_end(self):
        if not self.head:
            raise IndexError("underflow")
        if not self.head.next:
            v = self.head.data
            self.head = None
            return v
        cur = self.head
        while cur.next.next:
            cur = cur.next
        v = cur.next.data
        cur.next = None
        return v

    def delete_value(self, key):
        if not self.head:
            return False
        if self.head.data == key:
            self.head = self.head.next
            return True
        prev, cur = self.head, self.head.next
        while cur and cur.data != key:
            prev, cur = cur, cur.next
        if cur is None:
            return False
        prev.next = cur.next
        return True

    def search(self, key):
        cur, pos = self.head, 0
        while cur:
            if cur.data == key:
                return pos
            cur, pos = cur.next, pos + 1
        return -1

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_front(2); ll.insert_front(1); ll.insert_end(4)
    assert ll.insert_after(2, 3)
    assert ll.to_list() == [1, 2, 3, 4]
    assert ll.search(3) == 2 and ll.search(9) == -1
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]
    assert ll.delete_front() == 4 and ll.delete_end() == 1
    assert ll.delete_value(3) and ll.to_list() == [2]
    print("OK")
