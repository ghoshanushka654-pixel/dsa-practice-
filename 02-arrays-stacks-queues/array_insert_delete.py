"""
Topic: Array insertion, shifting and deletion (Module 2, high priority)
Problem: Insert x at position p and delete the element at position p in an array.
Source: Classic
Difficulty: Easy
Approach: Insert -> shift A[n-1]..A[p] one place right (start from the last!), then set A[p].
          Delete -> shift A[p+1]..A[n-1] one place left.
Time: O(n) worst (front), O(1) best (end)   Space: O(1)
"""


def insert_at(arr, n, pos, x):
    """arr has fixed capacity len(arr), n elements in use. Returns (new_n, shifts)."""
    if n == len(arr):
        raise OverflowError("array is full")
    if not 0 <= pos <= n:
        raise IndexError("invalid position")
    shifts = 0
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]
        shifts += 1
    arr[pos] = x
    return n + 1, shifts


def delete_at(arr, n, pos):
    """Returns (deleted_value, new_n, shifts)."""
    if n == 0:
        raise IndexError("array is empty")
    if not 0 <= pos < n:
        raise IndexError("invalid position")
    x = arr[pos]
    shifts = 0
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]
        shifts += 1
    arr[n - 1] = None
    return x, n - 1, shifts


if __name__ == "__main__":
    a = [10, 20, 30, 40, None, None]
    n, shifts = insert_at(a, 4, 0, 5)          # worst case: front
    assert a[:n] == [5, 10, 20, 30, 40] and shifts == 4
    n, shifts = insert_at(a, n, n, 50)         # best case: end
    assert a[:n] == [5, 10, 20, 30, 40, 50] and shifts == 0
    try:
        insert_at(a, n, 0, 1)
        raise AssertionError
    except OverflowError:
        pass
    x, n, shifts = delete_at(a, n, 0)
    assert x == 5 and a[:n] == [10, 20, 30, 40, 50] and shifts == 5
    print("OK")
