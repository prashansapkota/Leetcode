class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        final = []
        
        
        while left < right:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            elif (numbers[left] + numbers[right]) < target:
                left += 1
            else:
                final.append(left+1)
                final.append(right+1)
                right -= 1
                left += 1

        return final