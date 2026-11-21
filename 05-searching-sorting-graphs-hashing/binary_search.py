"""
Topic: Searching (Module 5)
Problem: Binary Search (iterative, recursive, first occurrence)
Source: LeetCode #704
Difficulty: Easy
Approach: Array must be sorted. Halve the range each step.
Time: O(log n)   Space: O(1) iterative, O(log n) recursive
"""


def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_rec(a, target, lo=0, hi=None):
    hi = len(a) - 1 if hi is None else hi
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    if a[mid] < target:
        return binary_search_rec(a, target, mid + 1, hi)
    return binary_search_rec(a, target, lo, mid - 1)


def first_occurrence(a, target):
    lo, hi, ans = 0, len(a) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            ans, hi = mid, mid - 1
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


if __name__ == "__main__":
    a = [-1, 0, 3, 5, 9, 12]
    assert binary_search(a, 9) == binary_search_rec(a, 9) == 4
    assert binary_search(a, 2) == binary_search_rec(a, 2) == -1
    assert first_occurrence([1, 2, 2, 2, 3], 2) == 1
    print("OK")
