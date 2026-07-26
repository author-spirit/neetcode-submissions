class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Naive-approach
        Search in target in all the rows

        Better approach
        Pattern: 2 binary search
        Invariant: If target exists, it will be within a row [0-N], 
                   where first integer in row is greater than last integer of prev row
        State: target fall within [top-bottom] adn the [left,right]
        Violates: When the target not in current interval
        Recover: discard the half of the row that do not contain target
        Time: O(log(m*n))

        Even Better approach
        Flatten the matrix and apply left = idx//cols, right = idx % cols 
        """

        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 20

        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            # search M - rows
            mid = (bottom + top)//2
            first = matrix[mid][0]
            last = matrix[mid][-1]

            if first == target or last == target:
                return True
            elif target > first and target < last:
                # search N - columns

                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    col_mid = (left + right)//2
                    value = matrix[mid][col_mid]
                    if matrix[mid][col_mid] == target:
                        return True
                    elif target > value:
                        left = col_mid + 1
                    else:
                        right = col_mid - 1
                return False
            elif target > last:
                top = mid + 1
            else:
                bottom = mid -1
        
        return False

        