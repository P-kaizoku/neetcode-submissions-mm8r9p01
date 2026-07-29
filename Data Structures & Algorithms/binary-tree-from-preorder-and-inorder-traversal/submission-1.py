# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {val: idx for idx, val in enumerate(inorder)}
        self.predex = 0

        def helper(left_i, right_i):
            if left_i > right_i:
                return None
            
            root_val = preorder[self.predex]
            self.predex += 1

            root = TreeNode(root_val)

            mid = mp[root_val]

            root.left = helper(left_i, mid-1)
            root.right = helper(mid+1, right_i)

            return root
        
        return helper(0, len(preorder)-1)
