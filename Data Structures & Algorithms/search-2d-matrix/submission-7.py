class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        end = len(matrix) - 1
        start = 0
        row = 0
        while start <= end:

            row = start + ((end - start) // 2)
            print("Start: ", start)
            print("Row: ", row)
            print("End: ", end)
            if matrix[row][-1] == target:
                print("Row: ", row)
                return True

            if matrix[row][-1] > target:
                print("Row: ", row)
                end = row - 1

            else:
                start = row + 1

        end = len(matrix[0]) - 1
        row = start
        start = 0

        if len(matrix) <= row:
            row = len(matrix) - 1
        while start <= end:
            mid = start + ((end - start) // 2)

            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] > target:
                end = mid - 1
            
            else:
                start = mid + 1
            
        return False
                

        