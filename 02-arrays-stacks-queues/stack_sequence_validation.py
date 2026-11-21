"""
Topic: Stack: push, pop and sequence questions (Module 2, high priority)
Problem: Push 1..n in order. Is a given pop sequence possible?
Source: Classic (e.g. push 1,2,3 -> 3 1 2 is impossible)
Difficulty: Medium
Approach: Simulate: push in order, pop whenever the top equals the next wanted value.
Time: O(n)   Space: O(n)
"""
from itertools import permutations


def is_valid_pop_sequence(push_order, pop_order):
    stack, j = [], 0
    for x in push_order:
        stack.append(x)
        while stack and j < len(pop_order) and stack[-1] == pop_order[j]:
            stack.pop()
            j += 1
    return j == len(pop_order)


if __name__ == "__main__":
    push = [1, 2, 3]
    assert not is_valid_pop_sequence(push, [3, 1, 2])
    for ok in ([3, 2, 1], [2, 1, 3], [1, 2, 3], [1, 3, 2], [2, 3, 1]):
        assert is_valid_pop_sequence(push, ok)
    # number of valid sequences for n items is the Catalan number: n=3 -> 5
    assert sum(is_valid_pop_sequence(push, list(p)) for p in permutations(push)) == 5
    print("OK")
