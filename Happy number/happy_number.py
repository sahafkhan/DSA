# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false



# Initialize a Tracker: A set named seen is created to keep track of all the numbers generated during the process. This is crucial for detecting cycles.

# Convert to String: The input number n is converted to a string (curr) to make it easier to iterate through each individual digit.

# Start a Loop: A while loop runs as long as the current number string has not been seen before. This prevents the code from running forever if it hits an infinite loop.

# Add to History: Inside the loop, the current string is added to the seen set.

# Calculate Digit Squares: * A variable summ is initialized to 0.

# A for loop iterates through every digit in the string.

# Each digit is converted back to an integer, squared, and added to the summ.

# Check for Success: * If the summ equals 1, the function immediately returns True because the number is "happy."

# Update and Repeat: If it’s not 1, the summ is converted back into a string and assigned to curr, and the process repeats.

# Handle Cycles: If the loop exits because a number is repeated (meaning it's back in the seen set), the function returns False because the number will loop endlessly without ever reaching 1.



class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = str(n)

        while curr not in seen:
            seen.add(curr)
            summ = 0
            for digit in curr:
                digit = int(digit)
                summ += digit **2
            
            if summ == 1:
                return True
            curr = str(summ)
        return False