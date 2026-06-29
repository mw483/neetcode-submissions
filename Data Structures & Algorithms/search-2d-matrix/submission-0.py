class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we have to: find the row where the target is
        # transform the 2d matrix into 1d, run binary search on the virtual 1d array
        row_num = len(matrix)
        col_num = len(matrix[0])
        low = 0
        high = (row_num * col_num) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            row = mid // col_num
            col = mid % col_num
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                high = mid - 1
            else:
                low = mid + 1
        return False 