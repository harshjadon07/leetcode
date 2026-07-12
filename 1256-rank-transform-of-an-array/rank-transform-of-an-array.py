from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        
        # Assign ranks to unique sorted elements
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i
        
        # Replace elements with their ranks
        return [rank[num] for num in arr]  