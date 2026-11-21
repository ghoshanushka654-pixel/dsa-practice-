"""
Problem: Reverse an array in place
Source: GeeksforGeeks (basic)
Difficulty: Easy
Approach: Two pointers swapping from both ends.
Time: O(n)   Space: O(1)
"""


def reverse(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


if __name__ == "__main__":
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse([]) == []
    print("OK")
