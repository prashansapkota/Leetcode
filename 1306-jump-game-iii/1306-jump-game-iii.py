class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visit = set([start])
        
        while queue:
            new_start = queue.popleft()

            if arr[new_start] == 0:
                return True

            left = new_start - arr[new_start]
            right = new_start + arr[new_start]

            for nxt in (left, right):
                if 0 <= nxt < len(arr) and nxt not in visit:
                    visit.add(nxt)
                    queue.append(nxt)

        return False

                
            
            
            
        
        