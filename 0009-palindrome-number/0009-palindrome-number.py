class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x!=0 and x % 10 == 0:
            return False

        x2 = str(x)
        left = 0
        right = len(x2) - 1

        while left < right:
            if x2[left] != x2[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True