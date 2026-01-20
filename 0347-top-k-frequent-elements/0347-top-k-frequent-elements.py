from collections import defaultdict
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = defaultdict(int)
        # for num in nums:
        #     counts[num] += 1
        # freq = list(counts.keys())
        # freq.sort(key=lambda freq: counts[freq], reverse = True)

        # final = []
        # for num in range(len(freq)):
        #     if len(final) < k:
        #         final.append(freq[num])
        # return final

        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        result = []
        for pair in heap:
            result.append(pair[1])
        return result


            


