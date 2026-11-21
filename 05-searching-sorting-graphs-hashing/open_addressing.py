"""
Topic: Hashing - open addressing (Module 5)
Problem: Hash table with linear or quadratic probing and deletion using tombstones.
Source: Classic
Difficulty: Medium
Approach: Linear:    index = (h + i) % m          Quadratic: index = (h + i*i) % m
          Deleting must leave a TOMBSTONE, otherwise later searches stop too early.
Time: avg O(1), worst O(m)   Space: O(m)
"""
DELETED = object()


class OpenAddressingTable:
    def __init__(self, m=7, probe="linear"):
        self.m, self.probe = m, probe
        self.table = [None] * m

    def _index(self, k, i):
        h = k % self.m
        return (h + i) % self.m if self.probe == "linear" else (h + i * i) % self.m

    def insert(self, k):
        for i in range(self.m):
            idx = self._index(k, i)
            if self.table[idx] is None or self.table[idx] is DELETED:
                self.table[idx] = k
                return idx
        raise OverflowError("hash table full")

    def search(self, k):
        for i in range(self.m):
            idx = self._index(k, i)
            if self.table[idx] is None:
                return -1
            if self.table[idx] == k:
                return idx
        return -1

    def delete(self, k):
        idx = self.search(k)
        if idx == -1:
            return False
        self.table[idx] = DELETED
        return True


if __name__ == "__main__":
    t = OpenAddressingTable(7, "linear")
    for k in (50, 700, 76, 85, 92, 73, 101):
        t.insert(k)
    assert t.table == [700, 50, 85, 92, 73, 101, 76]
    assert t.delete(85)
    assert t.search(92) == 3          # still found thanks to the tombstone
    assert t.search(85) == -1
    print("OK")
