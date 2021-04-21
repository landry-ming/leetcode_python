"""
二叉树的深度
关键点：树的最大深度等于其左子树的深度与右子树的深度中的最大值+1
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

### 层序遍历， 每遍历一层节点层数+1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res += 1
            queue = next_level
        return res


