import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for num in range(k):
            final = heapq.heappop(heap)
        return -final
            
                
        
        
                
        