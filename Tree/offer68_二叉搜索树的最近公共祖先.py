"""
找出公共祖先即找出两个节点的最近的公共根节点， 且若p是q的子节点， 则两者的公共祖先是q

假设root是p，q的最近公共祖先， 则只可能是以下几种情况：
1. p和q在root的子树中， 且分别位于两侧
2. p=root, q在root的左子树或者右子树中
3. q=root，p在root的左子树或者右子树中

方式一：迭代：
当节点root为空时跳出循环
当p,q都在root的右子树中则遍历至root.right
当p,q都在root的左子树中则遍历至root.left
否则， 则说明找到了公共祖先
返回root

时间复杂度：O(n), 其中N为二叉树的节点数， 每循环一次排除一层， 二叉搜索树的层数最小为logN(满二叉树)， 最大为N(退化为链表)
空间复杂度:O(1)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            if p.val < root.val and q.val < root.val:
                root = root.left
            else:
                break
        return root
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root