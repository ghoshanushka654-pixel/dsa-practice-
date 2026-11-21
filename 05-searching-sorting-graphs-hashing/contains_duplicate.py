"""
Topic: Hashing applications (Module 5)
Problem: Contains Duplicate
Source: LeetCode #217
Difficulty: Easy
Approach: Add each number to a set; if it is already there, there is a duplicate.
Time: O(n)   Space: O(n)
"""


def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1])
    assert not contains_duplicate([1, 2, 3, 4])
    print("OK")
