"""
Topic: Arrays and 2D address calculation (Module 2, high priority)
Problem: Find the memory address of A[i][j] in row-major and column-major order.
Source: Classic university numericals
Difficulty: Easy
Approach: B = base address, W = element size, M rows, N columns.
  1D:            LOC(A[i])    = B + W(i - LB)
  Row-major:     LOC(A[i][j]) = B + W[(i - LBr)*N + (j - LBc)]
  Column-major:  LOC(A[i][j]) = B + W[(j - LBc)*M + (i - LBr)]
Time: O(1)   Space: O(1)
"""


def addr_1d(B, W, i, LB=0):
    return B + W * (i - LB)


def addr_row_major(B, W, i, j, N, LBr=0, LBc=0):
    return B + W * ((i - LBr) * N + (j - LBc))


def addr_col_major(B, W, i, j, M, LBr=0, LBc=0):
    return B + W * ((j - LBc) * M + (i - LBr))


if __name__ == "__main__":
    # A[10][5], 0-based, B=1000, W=2, find A[3][2]
    assert addr_row_major(1000, 2, 3, 2, N=5) == 1034
    assert addr_col_major(1000, 2, 3, 2, M=10) == 1046
    # 1D: A[5] with LB=1, B=200, W=4
    assert addr_1d(200, 4, 5, LB=1) == 216
    # Non-zero lower bounds: A[1..4][1..3], B=100, W=1, A[3][2]
    assert addr_row_major(100, 1, 3, 2, N=3, LBr=1, LBc=1) == 107
    print("OK")
