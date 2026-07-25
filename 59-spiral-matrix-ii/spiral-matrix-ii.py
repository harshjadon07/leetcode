class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        # Start tracking the current value to insert
        num = 1
        
        while left <= right and top <= bottom:
            # 1. Fill top row (left to right)
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Shrink top boundary down
            
            # 2. Fill right column (top to bottom)
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Shrink right boundary left
            
            # 3. Fill bottom row (right to left)
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Shrink bottom boundary up
            
            # 4. Fill left column (bottom to top)
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Shrink left boundary right
            
        return matrix
