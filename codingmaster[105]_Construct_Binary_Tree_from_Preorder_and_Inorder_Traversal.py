class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = Node('F',
            Node('B',
                Node('A'),
                Node('D',
                    Node('C'),Node('E'))
                ),
            Node('G',
                None,
                Node('I', Node('H'))
                )
            )

# 전위순회 N=> target node L=> left R=> right
def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

preorder(root)

# 중위순회 LNR Left-> Node -> Right
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

inorder(root)

####### 책 풀이 #######
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node

####### 다른 풀이 #######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        import collections
        dictionary = {num:idx for idx, num in enumerate(inorder)}
        preorder_deque = collections.deque(preorder)

        def helper(start, end):
            if start>end: return None
            root_index = dictionary[preorder_deque.popleft()]
            root = TreeNode(inorder[root_index], helper(start, root_index-1), helper(root_index+1, end))
            return root
        return helper(0, len(preorder)-1)


a = [1,2,3]
len(a)
a[3:]

def test(a):
    if a == 1:
        return 'ok'
test(1)
print(test(2))
