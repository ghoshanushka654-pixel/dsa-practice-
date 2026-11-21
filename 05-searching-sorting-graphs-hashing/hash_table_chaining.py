"""
Topic: Hashing - collision handling by chaining (Module 5)
Problem: Hash table where each slot holds a list of keys.
Source: Classic
Difficulty: Easy-Medium
Approach: h(k) = k mod m. Colliding keys share a bucket list.
          Load factor alpha = n/m; average search O(1 + alpha).
Time: avg O(1), worst O(n)   Space: O(m + n)
"""


class ChainedHashTable:
    def __init__(self, m=7):
        self.m = m
        self.table = [[] for _ in range(m)]
        self.n = 0

    def _h(self, k):
        return k % self.m

    def insert(self, k):
        bucket = self.table[self._h(k)]
        if k not in bucket:
            bucket.append(k)
            self.n += 1

    def search(self, k):
        return k in self.table[self._h(k)]

    def delete(self, k):
        bucket = self.table[self._h(k)]
        if k in bucket:
            bucket.remove(k)
            self.n -= 1
            return True
        return False

    def load_factor(self):
        return self.n / self.m


if __name__ == "__main__":
    t = ChainedHashTable(7)
    for k in (50, 700, 76, 85, 92, 73, 101):
        t.insert(k)
    assert t.table[1] == [50, 85, 92]                # all hash to 1 -> chain
    assert t.search(92) and not t.search(8)
    assert t.delete(85) and not t.search(85)
    assert abs(t.load_factor() - 6 / 7) < 1e-9
    print("OK")
