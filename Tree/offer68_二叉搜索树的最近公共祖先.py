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
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
    
#### 非搜索树的首个共同祖先
"""
最近公共祖先发生的情况：若root是p，q的公共主先，则：
p和q在root的子树中，并在root的异侧
p = root，且q在p的左子树或者右子树中
q = root， 且p在q的左子树或者右子树中

递归条件：
1. 当越过叶子节点， 则返回null
2. 当root=p,q则直接返回p，q

递推工作
开始递归左节点，记为left
开始递归右节点， 记为right

返回值
当left和right同时为空， 说明pq均不在左右子树中，返回null
当left和right同时不为空，说明pq在异侧， 返回root
当left为空， right不为空，pq均不在root的左侧， 返回right
    1. p，q其中一个在右侧，此时right指向p或q
    2. p，q均在右侧，right指向公共祖先
left不为空，right为空也一样。

"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root