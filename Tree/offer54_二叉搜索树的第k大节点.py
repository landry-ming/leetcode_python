"""
二叉搜索树的中序遍历结果为递增序列， 那么中序结果的倒序就是递减序列
因此二叉搜索树第k大节点可转化为此树的中序遍历倒叙的第k个节点

中序遍历是左根右， 中序遍历的倒叙就是右根左

递归遍历时计数，统计当前节点的序号；
递归到第k个节点时，应记录结果 res ；
记录结果后，后续的遍历即失去意义，应提前终止（即返回）

终止条件：当节点为root的时候就应该返回， 当递归k次获取第k次结果后也应该返回
统计序号 k = k-1

当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 N ，占用 O(N) 时间。
空间复杂度 O(N) ： 当树退化为链表时（全部为右子节点），系统使用 O(N) 大小的栈空间。

"""

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            golbal k
            if not root:
                return
            
            dfs(root.right)
            if k == 0:
                return 
            k -= 1
            if k == 0:
                res = root.val
            dfs(root.left)
        dfs(root)
        return res