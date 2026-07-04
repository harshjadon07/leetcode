class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle empty string after spaces
        if i == n:
            return 0

        # Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0

        # Read digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Overflow check
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num