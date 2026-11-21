"""
Problem: Implement a Queue using two Stacks
Source: LeetCode #232
Difficulty: Easy
Approach: Push onto `inp`. For dequeue, if `out` is empty move everything from `inp`
          to `out` (this reverses the order, giving FIFO).
Time: amortized O(1)   Space: O(n)
"""


class MyQueue:
    def __init__(self):
        self.inp, self.out = [], []

    def push(self, x):
        self.inp.append(x)

    def _shift(self):
        if not self.out:
            while self.inp:
                self.out.append(self.inp.pop())

    def pop(self):
        self._shift()
        return self.out.pop()

    def peek(self):
        self._shift()
        return self.out[-1]

    def empty(self):
        return not self.inp and not self.out


if __name__ == "__main__":
    q = MyQueue()
    q.push(1); q.push(2)
    assert q.peek() == 1 and q.pop() == 1
    q.push(3)
    assert q.pop() == 2 and q.pop() == 3 and q.empty()
    print("OK")
