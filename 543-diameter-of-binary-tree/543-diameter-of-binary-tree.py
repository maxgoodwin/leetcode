# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.maxDiameter = 0
    self.dfs(root)
    
    return self.maxDiameter
    
  def dfs(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    
    leftMaxDepth = self.dfs(root.left)
    rightMaxDepth = self.dfs(root.right)
    
    self.maxDiameter = max(self.maxDiameter, leftMaxDepth + rightMaxDepth)
    
    return max(leftMaxDepth, rightMaxDepth) + 1