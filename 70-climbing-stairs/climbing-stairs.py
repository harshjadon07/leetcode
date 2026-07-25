class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way for 1 step, 2 ways for 2 steps
        if n <= 2:
            return n
        
        # Track the number of ways for the two preceding steps
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2
        
        # Calculate ways for steps from 3 up to n
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
