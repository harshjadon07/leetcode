import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total moves needed is (m - 1) + (n - 1)
        # We need to choose (m - 1) down moves out of total moves
        return math.comb(m + n - 2, m - 1)
