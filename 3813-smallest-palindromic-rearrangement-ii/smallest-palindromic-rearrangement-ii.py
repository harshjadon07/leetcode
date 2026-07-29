from collections import Counter
from math import comb
from typing import List

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""
        half_len = 0

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2
            half_len += cnt // 2

        LIMIT = k

        def count_permutations(cnt):
            rem = sum(cnt)
            res = 1
            for x in cnt:
                if x:
                    res *= comb(rem, x)
                    if res > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return res

        if count_permutations(half) < k:
            return ""

        first_half = []

        while half_len > 0:
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_permutations(half)

                if ways >= k:
                    first_half.append(chr(i + ord('a')))
                    half_len -= 1
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(first_half)
        return left + mid + left[::-1]