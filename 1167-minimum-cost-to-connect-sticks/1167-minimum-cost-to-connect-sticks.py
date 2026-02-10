import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = [num for num in sticks]
        heapq.heapify(heap)
        total = 0
        cost = 0
        if len(heap) == 1:
            return total
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            cost = x + y
            total += cost
            heapq.heappush(heap, cost)
        return total

            

