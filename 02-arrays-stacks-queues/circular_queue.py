"""
Topic: Queue: circular (Module 2, high priority)
Problem: Circular queue that reuses freed slots (fixes false overflow).
Source: Classic
Difficulty: Medium
Approach: rear = (rear+1) % N, front = (front+1) % N. One slot is kept unused so that
          empty: front == rear      full: (rear+1) % N == front
Time: O(1) per operation   Space: O(N) (capacity N-1)
"""


class CircularQueue:
    def __init__(self, n):
        self.q = [None] * n
        self.n = n
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.n == self.front

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue overflow")
        self.rear = (self.rear + 1) % self.n
        self.q[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue underflow")
        self.front = (self.front + 1) % self.n
        return self.q[self.front]


if __name__ == "__main__":
    q = CircularQueue(5)              # holds at most 4 items
    for x in (1, 2, 3, 4):
        q.enqueue(x)
    assert q.is_full()
    assert q.dequeue() == 1 and q.dequeue() == 2
    q.enqueue(5)
    q.enqueue(6)                      # reuses the freed slots (no false overflow)
    assert [q.dequeue() for _ in range(4)] == [3, 4, 5, 6]
    assert q.is_empty()
    print("OK")
