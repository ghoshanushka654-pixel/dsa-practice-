"""
Topic: Binary search tree (Module 4, high priority)
Problem: BST insert, search, delete (all 3 cases), min/max, validate.
Source: Classic / LeetCode #98, #450
Difficulty: Medium
Approach: Property: left subtree < node < right subtree; inorder gives sorted keys.
          Delete cases: (1) leaf -> remove; (2) one child -> replace by the child;
          (3) two children -> copy the inorder successor (min of right subtree),
          then delete that successor.
Time: O(h): O(log n) balanced, O(n) skewed   Space: O(h)
"""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    while root and root.key != key:
        root = root.left if key < root.key else root.right
    return root is not None


def min_node(root):
    while root.left:
        root = root.left
    return root


def max_node(root):
    while root.right:
        root = root.right
    return root


def delete(root, key):
    if not root:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = min_node(root.right)
        root.key = succ.key
        root.right = delete(root.right, succ.key)
    return root


def inorder(root):
    return [] if not root else inorder(root.left) + [root.key] + inorder(root.right)


def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if not root:
        return True
    return lo < root.key < hi and is_valid_bst(root.left, lo, root.key) \
        and is_valid_bst(root.right, root.key, hi)


if __name__ == "__main__":
    root = None
    for k in (50, 30, 70, 20, 40, 60, 80):
        root = insert(root, k)
    assert inorder(root) == [20, 30, 40, 50, 60, 70, 80] and is_valid_bst(root)
    assert search(root, 60) and not search(root, 65)
    assert min_node(root).key == 20 and max_node(root).key == 80
    root = delete(root, 20)          # case 1: leaf
    root = delete(root, 30)          # case 2: one child (40)
    root = delete(root, 50)          # case 3: two children -> successor 60
    assert root.key == 60 and inorder(root) == [40, 60, 70, 80] and is_valid_bst(root)
    print("OK")
