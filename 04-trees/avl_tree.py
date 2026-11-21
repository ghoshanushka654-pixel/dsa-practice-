"""
Topic: AVL tree and rotations (Module 4, high priority)
Problem: Self-balancing BST with insert and delete.
Source: Classic
Difficulty: Hard
Approach: Balance factor = height(left) - height(right) must stay in {-1, 0, 1}.
          LL -> right rotation       RR -> left rotation
          LR -> left rotate child, then right rotate
          RL -> right rotate child, then left rotate
Time: O(log n) per operation   Space: O(log n)
"""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right, self.height = key, None, None, 1


def h(n):
    return n.height if n else 0


def update(n):
    n.height = 1 + max(h(n.left), h(n.right))


def balance(n):
    return h(n.left) - h(n.right)


def rotate_right(y):
    x = y.left
    y.left, x.right = x.right, y
    update(y)
    update(x)
    return x


def rotate_left(x):
    y = x.right
    x.right, y.left = y.left, x
    update(x)
    update(y)
    return y


def rebalance(node):
    update(node)
    b = balance(node)
    if b > 1:
        if balance(node.left) < 0:                 # LR
            node.left = rotate_left(node.left)
        return rotate_right(node)                  # LL
    if b < -1:
        if balance(node.right) > 0:                # RL
            node.right = rotate_right(node.right)
        return rotate_left(node)                   # RR
    return node


def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return rebalance(node)


def delete(node, key):
    if not node:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        succ = node.right
        while succ.left:
            succ = succ.left
        node.key = succ.key
        node.right = delete(node.right, succ.key)
    return rebalance(node)


def inorder(n):
    return [] if not n else inorder(n.left) + [n.key] + inorder(n.right)


def is_avl(n):
    """Re-computes heights and checks every balance factor."""
    if not n:
        return 0
    lh, rh = is_avl(n.left), is_avl(n.right)
    if lh < 0 or rh < 0 or abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)


if __name__ == "__main__":
    def build(keys):
        r = None
        for k in keys:
            r = insert(r, k)
        return r

    r = build([10, 20, 30])                        # RR -> left rotation
    assert (r.key, r.left.key, r.right.key) == (20, 10, 30)
    assert build([30, 20, 10]).key == 20           # LL
    assert build([30, 10, 20]).key == 20           # LR
    assert build([10, 30, 20]).key == 20           # RL
    r = build(range(1, 16))                        # sorted input stays balanced
    assert r.key == 8 and r.height == 4 and is_avl(r) > 0
    for k in (1, 2, 3, 4, 5):
        r = delete(r, k)
        assert is_avl(r) > 0
    assert inorder(r) == list(range(6, 16))
    print("OK")
