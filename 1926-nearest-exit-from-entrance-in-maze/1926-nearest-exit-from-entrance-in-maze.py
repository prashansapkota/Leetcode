from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r, c = entrance
        queue = deque([(r, c)])
        seen = {(r, c)}
        ans = 0
        directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        rows = len(maze)
        cols = len(maze[0])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                
                r, c = queue.popleft()

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                        
                    if maze[nr][nc] == "+":
                        continue
                        
                    if (nr, nc) in seen:
                        continue
                    
                    if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1):
                        return ans + 1

                    seen.add((nr, nc))
                    queue.append((nr, nc))
        
            ans += 1
        return -1
                
            
            
            