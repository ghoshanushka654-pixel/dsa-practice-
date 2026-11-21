"""
Topic: Searching (Module 5)
Problem: Linear Search (first and all occurrences)
Source: Classic
Difficulty: Easy
Approach: Scan left to right.
Time: O(n) worst, O(1) best   Space: O(1)
"""


def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def find_all(arr, target):
    return [i for i, x in enumerate(arr) if x == target]


if __name__ == "__main__":
    assert linear_search([4, 2, 7, 2], 2) == 1
    assert linear_search([4, 2, 7], 9) == -1
    assert find_all([4, 2, 7, 2], 2) == [1, 3]
    print("OK")
