class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        if new == "":
            return True

        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] == new[right]:
                left+=1
                right-=1
            else:
                return False
        return True

        