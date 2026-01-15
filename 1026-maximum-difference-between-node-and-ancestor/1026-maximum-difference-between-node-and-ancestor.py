# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_min, cur_max):
            if not node:
                return 0

            # difference with ancestors
            diff = max(
                abs(node.val - cur_min),
                abs(node.val - cur_max)
            )

            # update min and max
            new_min = min(cur_min, node.val)
            new_max = max(cur_max, node.val)

            # go deeper
            left = dfs(node.left, new_min, new_max)
            right = dfs(node.right, new_min, new_max)

            return max(diff, left, right)

        return dfs(root, root.val, root.val)



        