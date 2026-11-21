"""
Topic: Binary tree insert, search and delete (Module 4)
Problem: Operations on an (unordered) binary tree.
Source: Classic
Difficulty: Medium
Approach: Search -> any traversal, O(n).  Insert -> level-order, first vacant child.
          Delete -> copy the deepest-rightmost node's value into the target node,
          then remove that deepest node.
Time: O(n) each   Space: O(n)
"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None


def insert(root, val):
    if not root:
        return Node(val)
    q = deque([root])
    while q:
        n = q.popleft()
        if not n.left:
            n.left = Node(val)
            return root
        q.append(n.left)
        if not n.right:
            n.right = Node(val)
            return root
        q.append(n.right)


def search(root, key):
    if not root:
        return False
    return root.val == key or search(root.left, key) or search(root.right, key)


def delete(root, key):
    if not root:
        return None
    if not root.left and not root.right:
        return None if root.val == key else root
    target, last, parent = None, None, {}
    q = deque([root])
    while q:
        last = q.popleft()
        if last.val == key and target is None:
            target = last
        for child in (last.left, last.right):
            if child:
                parent[child] = last
                q.append(child)
    if target is None:
        return root
    target.val = last.val                      # deepest rightmost value
    p = parent[last]
    if p.right is last:
        p.right = None
    else:
        p.left = None
    return root


def inorder(r):
    return [] if not r else inorder(r.left) + [r.val] + inorder(r.right)


if __name__ == "__main__":
    root = None
    for v in range(1, 6):
        root = insert(root, v)
    assert inorder(root) == [4, 2, 5, 1, 3]
    assert search(root, 5) and not search(root, 9)
    root = delete(root, 2)                     # 5 (deepest rightmost) replaces 2
    assert inorder(root) == [4, 5, 1, 3]
    print("OK")
