"""
Topic: Time-space trade-off (Module 1)
Problem: Compute Fibonacci numbers; compare recomputing vs storing results.
Source: Classic
Difficulty: Easy
Approach: Naive recursion recomputes subproblems (little memory, lots of time).
          Memoization stores results in a table (more memory, far less time).
Time: naive O(2^n), memo O(n)   Space: naive O(n) stack, memo O(n) table
"""


def fib_naive(n, counter):
    counter[0] += 1
    if n < 2:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, memo, counter):
    if n in memo:
        return memo[n]
    counter[0] += 1
    memo[n] = n if n < 2 else fib_memo(n - 1, memo, counter) + fib_memo(n - 2, memo, counter)
    return memo[n]


def square_queries(queries, limit):
    """Precompute i*i for all i<=limit (O(limit) space) so each query is O(1)."""
    table = [i * i for i in range(limit + 1)]
    return [table[q] for q in queries]


if __name__ == "__main__":
    c1, c2 = [0], [0]
    assert fib_naive(20, c1) == fib_memo(20, {}, c2) == 6765
    print("naive calls:", c1[0], "| memo computations:", c2[0])  # 21891 vs 21
    assert c1[0] == 21891 and c2[0] == 21
    assert square_queries([3, 7, 10], 10) == [9, 49, 100]
    print("OK")
