import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles] 
        heapq.heapify(heap) 
        ans = 0 
        for i in range(len(piles)): 
            ans += piles[i] 
        for i in range(k): 
            x = heapq.heappop(heap)
            ans -= floor(abs(x) / 2)
            heapq.heappush(heap, floor(x / 2))
        return ans
                
        
        
        
        