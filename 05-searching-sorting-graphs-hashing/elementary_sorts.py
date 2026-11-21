"""
Topic: Bubble, selection and insertion sort (Module 5, high priority)
Problem: Implement the three O(n^2) sorts and compare their behaviour.
Source: Classic
Difficulty: Easy
Approach:
  Bubble    swap adjacent out-of-order pairs; swap flag gives best case O(n); stable.
  Selection pick the minimum of the unsorted part, swap into place; O(n^2) always;
            at most n-1 swaps; NOT stable.
  Insertion insert A[i] into the sorted prefix by shifting; best O(n); stable.
Time: worst O(n^2)   Space: O(1)
"""


def bubble_sort(a, key=lambda x: x):
    a, passes = list(a), 0
    for i in range(len(a) - 1):
        swapped = False
        passes += 1
        for j in range(len(a) - 1 - i):
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, passes


def selection_sort(a, key=lambda x: x):
    a = list(a)
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if key(a[j]) < key(a[m]):
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def insertion_sort(a, key=lambda x: x):
    a = list(a)
    for i in range(1, len(a)):
        cur, j = a[i], i - 1
        while j >= 0 and key(a[j]) > key(cur):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(data)[0] == selection_sort(data) == insertion_sort(data) == sorted(data)
    assert bubble_sort([1, 2, 3, 4])[1] == 1          # best case: one pass
    pairs = [(2, "a"), (2, "b"), (1, "c")]
    k = lambda t: t[0]
    assert bubble_sort(pairs, k)[0] == [(1, "c"), (2, "a"), (2, "b")]     # stable
    assert insertion_sort(pairs, k) == [(1, "c"), (2, "a"), (2, "b")]     # stable
    assert selection_sort(pairs, k) == [(1, "c"), (2, "b"), (2, "a")]     # NOT stable
    print("OK")
