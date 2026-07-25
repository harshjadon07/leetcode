import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Convert k to 0-indexed to match array tracking
        k -= 1
        
        # Build the pool of available digits: [1, 2, ..., n]
        numbers = list(range(1, n + 1))
        
        # Precompute the factorial for (n - 1)
        factorial = math.factorial(n - 1)
        
        result = []
        
        # Construct the permutation character by character
        for i in range(n - 1, 0, -1):
            # Find the index of the block k falls into
            index = k // factorial
            result.append(str(numbers.pop(index)))
            
            # Reduce k to find the position within the current block
            k %= factorial
            
            # Update the factorial for the next position
            factorial //= i
            
        # Append the final remaining digit
        result.append(str(numbers[0]))
        
        return "".join(result)
