class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Iterate from the rightmost digit to the leftmost
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Early return if no carry propagates further
            
            digits[i] = 0  # If the digit is 9, it becomes 0 and carry continues
        
        # If the loop finishes, all digits were 9 (e.g., [9, 9, 9] -> [0, 0, 0])
        return [1] + digits
