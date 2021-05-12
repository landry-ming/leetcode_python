"""
这题主要是需要得到叶子节点的值
可以使用深度优先搜索，总是先搜索节点的左节点， 再深度搜索叶子节点的右节点
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if not root.left and not root.right:
                yield root.val
            if root.left:
                yield from dfs(root.left)
            if root.right:
                yield from dfs(root.right)
        list1 = list(dfs(root1)) if root1 else []
        list2 = list(dfs(root2)) if root2 else []
        return list1 == list2

"""
迭代的方法即前序遍历
"""
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preorder(root):
            if not root:
                return []
            res = []
            queue = [root]
            while queue:
                cur = queue.pop()
                if not cur.left and not cur.right:
                    res.append(cur.val)
                else:
                    if cur.right:
                        queue.append(cur.right)
                    if cur.left:
                        queue.append(cur.left)
            return res
        return preorder(root1) == preorder(root2)
