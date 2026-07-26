class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Naive-approach
        Search in target in all the rows

        Better approach
        Invariant: The target will always be within a row [0-N], 
                   where first integer in row is greater than last integer of prev row
        State: Interval containing row[0-N][0] - where target fall within [top-bottom]
        Violates: When the target not in current interval
        Recover: move to next interval when target >= row[N][0] or target <= row[N][N]
        """

        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 20

        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            # search M - rows
            mid = (bottom + top)//2
            first = matrix[mid][0]
            last = matrix[mid][-1]

            print("Row", mid, matrix[mid], (first, last))

            if first == target or last == target:
                return True
            elif target > first and target < last:
                # search N - columns

                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    col_mid = (left + right)//2
                    if matrix[mid][col_mid] == target:
                        return True
                    elif target > col_mid:
                        left = col_mid + 1
                    else:
                        right = col_mid - 1
                return False
            elif target > last:
                top = mid + 1
            else:
                bottom = mid -1
        
        return False

        