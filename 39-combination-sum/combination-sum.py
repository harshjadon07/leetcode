from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remain - candidates[i])  # reuse same candidate
                path.pop()

        backtrack(0, [], target)
        return res