"""
Topic: Stack applications (Module 2)
Problem: Valid Parentheses
Source: LeetCode #20
Difficulty: Easy
Approach: Push opening brackets; on a closing bracket the top must match.
Time: O(n)   Space: O(n)
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    assert is_valid("()[]{}") and is_valid("{[()]}")
    assert not is_valid("(]") and not is_valid("((") and not is_valid("]")
    print("OK")
