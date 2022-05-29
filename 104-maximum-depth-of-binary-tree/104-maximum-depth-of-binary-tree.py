# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    return self.dfs(root, 0)
    
  def dfs(self, root: Optional[TreeNode], depth: int) -> int:
    if root == None:
      return depth
    
    leftDepth = self.dfs(root.left, depth + 1)
    rightDepth = self.dfs(root.right, depth + 1)
    
    return max(leftDepth, rightDepth)