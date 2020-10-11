class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        lower = 0
        upper = len(matrix) - 1
        while lower <= upper:

            mid = lower + (upper - lower) // 2
            if target == matrix[mid][0]:
                return True
            if target > matrix[mid][0]:
                lower = mid + 1
            else:
                upper = mid - 1##先搜索哪一行，二分搜索取左边界

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(upper, mid)
            if target == matrix[upper][mid]:
                return True
            if target < matrix[upper][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False


s = Solution()
a = [[1]]
b = 3
print(s.searchMatrix(a, b))
