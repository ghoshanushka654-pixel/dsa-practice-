"""
Topic: Graph terminology, BFS and DFS (Module 5)
Problem: Adjacency-list graph with BFS, DFS (recursive + iterative), shortest path
         (fewest edges), connected components and cycle detection.
Source: Classic
Difficulty: Medium
Approach: BFS = queue, mark visited when ENQUEUED, gives shortest path by edge count.
          DFS = recursion or stack. Sum of degrees = 2|E|.
Time: O(V+E)   Space: O(V)
"""
from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, s):
        seen, order, q = {s}, [], deque([s])
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return order

    def dfs(self, s):
        seen, order = set(), []

        def go(u):
            seen.add(u)
            order.append(u)
            for v in self.adj[u]:
                if v not in seen:
                    go(v)
        go(s)
        return order

    def dfs_iterative(self, s):
        seen, order, stack = set(), [], [s]
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            order.append(u)
            stack.extend(reversed(self.adj[u]))
        return order

    def shortest_path(self, s, t):
        parent, q = {s: None}, deque([s])
        while q:
            u = q.popleft()
            if u == t:
                break
            for v in self.adj[u]:
                if v not in parent:
                    parent[v] = u
                    q.append(v)
        if t not in parent:
            return []
        path = []
        while t is not None:
            path.append(t)
            t = parent[t]
        return path[::-1]

    def components(self):
        seen, count = set(), 0
        for s in range(self.n):
            if s not in seen:
                seen.update(self.bfs(s))
                count += 1
        return count

    def has_cycle(self):
        seen = set()

        def go(u, parent):
            seen.add(u)
            for v in self.adj[u]:
                if v not in seen:
                    if go(v, u):
                        return True
                elif v != parent:
                    return True
            return False
        return any(go(s, -1) for s in range(self.n) if s not in seen)


if __name__ == "__main__":
    g = Graph(5)
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]:
        g.add_edge(u, v)
    assert g.bfs(0) == [0, 1, 2, 3, 4]
    assert g.dfs(0) == g.dfs_iterative(0) == [0, 1, 3, 2, 4]
    assert g.shortest_path(0, 4) == [0, 1, 3, 4]
    assert g.has_cycle() and g.components() == 1
    assert sum(len(a) for a in g.adj) == 2 * 5            # sum of degrees = 2|E|
    t = Graph(5)
    t.add_edge(0, 1); t.add_edge(1, 2); t.add_edge(3, 4)
    assert not t.has_cycle() and t.components() == 2
    print("OK")
