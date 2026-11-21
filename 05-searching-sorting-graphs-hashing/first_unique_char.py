"""
Topic: Hashing applications (Module 5)
Problem: First Unique Character in a String
Source: LeetCode #387
Difficulty: Easy
Approach: Count frequencies in a hash map, then return the first char with count 1.
Time: O(n)   Space: O(1) (fixed alphabet)
"""
from collections import Counter


def first_unique_char(s):
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    print("OK")
