"""
Topic: ADT and its operations; Stack push/pop (Module 2)
Problem: Implement a fixed-capacity Stack ADT with overflow and underflow checks.
Source: Classic
Difficulty: Easy
Approach: Array + top index. The ADT says WHAT (push, pop, peek, is_empty, is_full);
          the array is HOW.
Time: every operation O(1)   Space: O(capacity)
"""


class Stack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, x):
        if self.is_full():
            raise OverflowError("stack overflow")
        self.top += 1
        self.data[self.top] = x

    def pop(self):
        if self.is_empty():
            raise IndexError("stack underflow")
        x = self.data[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.data[self.top]


if __name__ == "__main__":
    s = Stack(3)
    for x in (1, 2, 3):
        s.push(x)
    assert s.is_full() and s.peek() == 3
    try:
        s.push(4)
        raise AssertionError
    except OverflowError:
        pass
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]
    try:
        s.pop()
        raise AssertionError
    except IndexError:
        pass
    print("OK")
