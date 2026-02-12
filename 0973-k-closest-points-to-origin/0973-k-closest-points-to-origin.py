import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = sqrt((point[0])**2 +(point[1])**2)
            heap.append((distance, point))
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            popped = heappop(heap)
            ans.append(popped[1])
        
        return ans
            
            
            
            
        
        
        
            
        
            