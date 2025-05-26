from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int):
    if not matrix or not matrix[0]:
      return False
    
    m, n = len(matrix), len(matrix[0])
    left = 0
    right = m * n - 1

    while (left <= right):
      mid = left + (right - left) // 2
      i = mid // n
      j = mid % n

      if matrix[i][j] == target:
        return True
      if matrix[i][j] < target:
        left = mid + 1
      else:
        right = mid - 1
    return False
  
sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 13

print(sol.searchMatrix(matrix, target))
print(sol.searchMatrix(matrix1, target1))