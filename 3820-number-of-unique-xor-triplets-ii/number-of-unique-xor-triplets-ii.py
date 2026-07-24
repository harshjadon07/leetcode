class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048

        dp = [[False] * MAXX for _ in range(4)]
        dp[0][0] = True

        for t in range(3):
            for x in range(MAXX):
                if dp[t][x]:
                    for v in nums:
                        dp[t + 1][x ^ v] = True

        return sum(dp[3])