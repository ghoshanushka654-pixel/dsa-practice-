"""
Topic: Quick sort (Module 5, high priority)
Problem: Quick Sort (Lomuto partition) and its worst case
Source: Classic
Difficulty: Medium
Approach: Partition around a pivot (smaller left, larger right), recurse on both sides.
          With the LAST element as pivot, already sorted input is the worst case:
          n(n-1)/2 comparisons.
Time: average O(n log n), worst O(n^2)   Space: O(log n) average stack
"""


def quick_sort(a, lo=0, hi=None, stats=None):
    """Sorts in place. stats[0] counts comparisons."""
    hi = len(a) - 1 if hi is None else hi
    stats = [0] if stats is None else stats
    if lo < hi:
        pivot, i = a[hi], lo
        for j in range(lo, hi):
            stats[0] += 1
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        quick_sort(a, lo, i - 1, stats)
        quick_sort(a, i + 1, hi, stats)
    return stats[0]


if __name__ == "__main__":
    a = [10, 7, 8, 9, 1, 5]
    quick_sort(a)
    assert a == [1, 5, 7, 8, 9, 10]
    worst = list(range(8))                      # sorted input
    assert quick_sort(worst) == 8 * 7 // 2      # 28 comparisons = n(n-1)/2
    print("OK")
