"""
Topic: Queue: linear (Module 2, high priority)
Problem: Array-based linear queue and its "false overflow" problem.
Source: Classic
Difficulty: Easy
Approach: ENQUEUE: if rear == N-1 -> overflow; rear++.  DEQUEUE: front++.
          False overflow: rear is at the end although slots at the front are free.
Time: O(1) per operation   Space: O(N)
"""


class LinearQueue:
    def __init__(self, n):
        self.q = [None] * n
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def enqueue(self, x):
        if self.rear == len(self.q) - 1:
            raise OverflowError("queue overflow")
        self.rear += 1
        self.q[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue underflow")
        x = self.q[self.front]
        self.front += 1
        return x


if __name__ == "__main__":
    q = LinearQueue(3)
    for x in (1, 2, 3):
        q.enqueue(x)
    assert q.dequeue() == 1 and q.dequeue() == 2
    try:
        q.enqueue(4)      # 2 free slots at the front, but still overflow!
        raise AssertionError
    except OverflowError:
        print("false overflow demonstrated")
    print("OK")
