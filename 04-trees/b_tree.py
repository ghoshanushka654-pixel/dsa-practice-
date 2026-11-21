"""
Topic: B-tree insert and delete (Module 4)
Problem: B-tree with search, insertion (with node splitting) and traversal.
Source: Classic (CLRS-style, minimum degree t)
Difficulty: Hard
Approach: Minimum degree t: every node holds at most 2t-1 keys; non-root nodes hold
          at least t-1. Insert goes down to a leaf; a full node is split at the median
          (the median key moves up) BEFORE descending into it. All leaves stay on the
          same level. NOTE: conventions for "order" differ - follow your class notes.
          TODO (practice): implement delete (borrow / merge cases).
Time: O(log n)   Space: O(n)
"""
from bisect import insort


class BTreeNode:
    def __init__(self, leaf):
        self.keys, self.children, self.leaf = [], [], leaf


class BTree:
    def __init__(self, t=2):
        self.t = t
        self.root = BTreeNode(True)

    def search(self, k, node=None):
        node = node or self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == k:
            return node, i
        return None if node.leaf else self.search(k, node.children[i])

    def _split_child(self, parent, i):
        t, y = self.t, parent.children[i]
        z = BTreeNode(y.leaf)
        median = y.keys[t - 1]
        z.keys, y.keys = y.keys[t:], y.keys[:t - 1]
        if not y.leaf:
            z.children, y.children = y.children[t:], y.children[:t]
        parent.keys.insert(i, median)
        parent.children.insert(i + 1, z)

    def insert(self, k):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(False)
            s.children = [r]
            self.root = s
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _insert_nonfull(self, x, k):
        if x.leaf:
            insort(x.keys, k)
            return
        i = len(x.keys) - 1
        while i >= 0 and k < x.keys[i]:
            i -= 1
        i += 1
        if len(x.children[i].keys) == 2 * self.t - 1:
            self._split_child(x, i)
            if k > x.keys[i]:
                i += 1
        self._insert_nonfull(x.children[i], k)

    def traverse(self, node=None):
        node = node or self.root
        out = []
        for i, key in enumerate(node.keys):
            if not node.leaf:
                out += self.traverse(node.children[i])
            out.append(key)
        if not node.leaf:
            out += self.traverse(node.children[-1])
        return out

    def check(self):
        """Verify B-tree properties; returns the leaf depth."""
        def walk(node, depth, is_root):
            assert len(node.keys) <= 2 * self.t - 1
            if not is_root:
                assert len(node.keys) >= self.t - 1
            if node.leaf:
                return depth
            assert len(node.children) == len(node.keys) + 1
            depths = {walk(c, depth + 1, False) for c in node.children}
            assert len(depths) == 1, "leaves not on the same level"
            return depths.pop()
        return walk(self.root, 0, True)


if __name__ == "__main__":
    bt = BTree(t=2)
    for k in range(1, 21):
        bt.insert(k)
        bt.check()
    assert bt.traverse() == list(range(1, 21))
    assert bt.search(13) is not None and bt.search(99) is None
    print("OK")
