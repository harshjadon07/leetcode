from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries):
        MOD = 10**9 + 7

        n = len(s)

        # Prefix sum of non-zero digits
        pref = [0] * (n + 1)
        nz_pos = []
        nz_digit = []

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            pref[i + 1] = pref[i]
            if d:
                pref[i + 1] += d
                nz_pos.append(i)
                nz_digit.append(d)

        k = len(nz_digit)

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix value of concatenated non-zero digits
        hashv = [0] * (k + 1)
        for i in range(k):
            hashv[i + 1] = (hashv[i] * 10 + nz_digit[i]) % MOD

        ans = []

        for l, r in queries:
            left = bisect_left(nz_pos, l)
            right = bisect_right(nz_pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            # Concatenated number modulo MOD
            num = (
                hashv[right + 1]
                - hashv[left] * pow10[length]
            ) % MOD

            digit_sum = pref[r + 1] - pref[l]

            ans.append((num * digit_sum) % MOD)

        return ans