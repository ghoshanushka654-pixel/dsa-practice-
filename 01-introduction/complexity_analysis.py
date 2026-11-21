"""
Topic: Complexity analysis and loops (Module 1)
Problem: Count how many times common loop patterns run, to see n, log n, log log n, n^2.
Source: Classic exam questions
Difficulty: Easy
Approach: Run each loop and count iterations; compare with the formula.
Time: see each function
"""


def linear(n):            # i = i + c         -> Theta(n)
    i, c = 0, 0
    while i < n:
        i += 1
        c += 1
    return c


def logarithmic(n):       # i = i * 2         -> Theta(log n)
    i, c = 1, 0
    while i <= n:
        i *= 2
        c += 1
    return c


def log_log(n):           # i = i * i         -> Theta(log log n)
    i, c = 2, 0
    while i <= n:
        i = i * i
        c += 1
    return c


def triangular(n):        # j from 1 to i     -> n(n+1)/2 = Theta(n^2)
    c = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            c += 1
    return c


def n_log_n(n):           # outer n, inner doubles -> Theta(n log n)
    c = 0
    for _ in range(n):
        j = 1
        while j <= n:
            j *= 2
            c += 1
    return c


def recurrence_t(n):      # T(n) = T(n-1) + n  -> n(n+1)/2 = Theta(n^2)
    return 0 if n == 0 else recurrence_t(n - 1) + n


if __name__ == "__main__":
    assert linear(16) == 16
    assert logarithmic(16) == 5            # i = 1,2,4,8,16
    assert log_log(65536) == 5             # i = 2,4,16,256,65536
    assert triangular(10) == 55
    assert n_log_n(16) == 16 * 5
    assert recurrence_t(10) == 55
    print("OK")
