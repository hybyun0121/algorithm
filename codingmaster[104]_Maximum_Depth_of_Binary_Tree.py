# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from types import *

class Solution:
    def maxDepth(self, root: TreeNode) -> int:



root = [3,9,20, None, None, 15,7]
sol = Solution()
sol.maxDepth(root)
