class Solution:
    def isPalindrome(self, x: int) -> bool:
                # Negative numbers or numbers ending with 0 (except 0)
        
        #updated 3
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            x //= 10

        # Even length: x == reversed_half
        # Odd length: x == reversed_half without middle digit
        return x == reversed_half or x == reversed_half // 10