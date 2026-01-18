# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        level = 0
        while queue:
            current_length = len(queue)
            # do logic for current level
            level_sum = []

            for _ in range(current_length):        
                node = queue.popleft()
                # do logic
                level_sum.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                ans.append(level_sum)
            else:
                ans.append(level_sum[::-1])
            level += 1
        return ans
        