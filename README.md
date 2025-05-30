# 2d-matrix-python

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m \* n)) time complexity.

================= Solution ==============
class Solution:
def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
if not matrix:
return False

    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = m * n

    while l < r:
      mid = (l + r) // 2
      i = mid // n
      j = mid % n
      if matrix[i][j] == target:
        return True
      if matrix[i][j] < target:
        l = mid + 1
      else:
        r = mid

    return False
