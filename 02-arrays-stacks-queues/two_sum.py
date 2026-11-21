"""
Problem: Two Sum
Source: LeetCode #1
Difficulty: Easy
Approach: Hash map of seen numbers; look up target - current.
Time: O(n)   Space: O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("OK")
