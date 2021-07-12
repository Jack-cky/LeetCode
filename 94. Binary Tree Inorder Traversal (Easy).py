# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root_node):
            if not root_node:
                return
            dfs(root_node.left)
            in_order.append(root_node.val)
            dfs(root_node.right)
        result = []
        dfs(root)
        return result