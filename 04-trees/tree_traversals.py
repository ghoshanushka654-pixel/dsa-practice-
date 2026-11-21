"""
Topic: Trees: terminology, proofs and traversals (Module 4, high priority)
Problem: Preorder, inorder, postorder, level-order traversals; height, node/leaf counts.
Source: Classic
Difficulty: Easy-Medium
Approach: Preorder = root,L,R   Inorder = L,root,R   Postorder = L,R,root
          Level-order uses a queue.  Height of a leaf = 0 (empty tree = -1).
          Facts checked: n nodes -> n-1 edges; leaves = (degree-2 nodes) + 1.
Time: O(n)   Space: O(h)
"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def preorder(r):
    return [] if not r else [r.val] + preorder(r.left) + preorder(r.right)


def inorder(r):
    return [] if not r else inorder(r.left) + [r.val] + inorder(r.right)


def postorder(r):
    return [] if not r else postorder(r.left) + postorder(r.right) + [r.val]


def inorder_iterative(r):
    out, stack, cur = [], [], r
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def level_order(r):
    out, q = [], deque([r] if r else [])
    while q:
        n = q.popleft()
        out.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return out


def height(r):
    return -1 if not r else 1 + max(height(r.left), height(r.right))


def count_nodes(r):
    return 0 if not r else 1 + count_nodes(r.left) + count_nodes(r.right)


def count_leaves(r):
    if not r:
        return 0
    return 1 if not r.left and not r.right else count_leaves(r.left) + count_leaves(r.right)


def count_degree2(r):
    if not r:
        return 0
    return (1 if r.left and r.right else 0) + count_degree2(r.left) + count_degree2(r.right)


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert preorder(root) == [1, 2, 4, 5, 3]
    assert inorder(root) == inorder_iterative(root) == [4, 2, 5, 1, 3]
    assert postorder(root) == [4, 5, 2, 3, 1]
    assert level_order(root) == [1, 2, 3, 4, 5]
    assert height(root) == 2 and count_nodes(root) == 5
    assert count_leaves(root) == count_degree2(root) + 1 == 3
    print("OK")
