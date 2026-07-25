class Solution:
    def isNumber(self, s: str) -> bool:
        # Initialize tracking flags
        seen_num = False
        seen_dot = False
        seen_e = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_num = True
            elif c in '+-':
                # Signs can only appear at index 0 or immediately after 'e'/'E'
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c in 'eE':
                # Exponent can only appear once and must follow a valid number
                if seen_e or not seen_num:
                    return False
                seen_e = True
                seen_num = False  # Reset to ensure digits follow the exponent
            elif c == '.':
                # Decimal point can only appear once and cannot be after an exponent
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            else:
                # Any other character is immediately invalid
                return False
                
        return seen_num
