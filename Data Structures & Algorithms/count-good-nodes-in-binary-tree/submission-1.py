# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxN):
            if not node:
                return 0
            
            good = 1 if maxN <= node.val else 0

            maxN = max(maxN, node.val)

            return (
                good +
                dfs(node.left, maxN) +
                dfs(node.right, maxN)
            )

        return dfs(root, root.val)