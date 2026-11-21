"""
Topic: Merge sort (Module 5, high priority)
Problem: Merge Sort
Source: Classic
Difficulty: Medium
Approach: Split into halves, sort each, merge. T(n) = 2T(n/2) + n.
          Taking from the LEFT half on ties keeps it stable.
Time: Theta(n log n) in all cases   Space: O(n)
"""


def merge_sort(a, key=lambda x: x):
    if len(a) <= 1:
        return list(a)
    mid = len(a) // 2
    left, right = merge_sort(a[:mid], key), merge_sort(a[mid:], key)
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(data) == sorted(data)
    assert merge_sort([]) == [] and merge_sort([1]) == [1]
    pairs = [(2, "a"), (1, "x"), (2, "b"), (1, "y")]
    assert merge_sort(pairs, key=lambda t: t[0]) == [(1, "x"), (1, "y"), (2, "a"), (2, "b")]
    print("OK")
