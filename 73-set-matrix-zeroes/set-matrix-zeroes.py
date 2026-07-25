class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # Flags to check if the first row or first column need to be zeroed
        first_row_zero = False
        first_col_zero = False
        
        # 1. Determine if first row or first col originally contain any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
                
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # 2. Use first row and first column to flag zeros for the inner matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 3. Update the inner matrix cells based on the flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 4. Finalize the first row if it originally had a zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # 5. Finalize the first column if it originally had a zero
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

