"""
Problem: Maximum Subarray (Kadane's Algorithm)
Source: LeetCode #53
Difficulty: Medium
Approach: Best sum ending at each index = max(element, previous best + element).
Time: O(n)   Space: O(1)
"""


def max_subarray(nums):
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([-3, -1, -2]) == -1
    print("OK")
