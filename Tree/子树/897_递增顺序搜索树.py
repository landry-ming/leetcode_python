"""
数组保存中序遍历的结果
时间复杂度o(n)：为二叉搜索树的节点总数
空间复杂度o(n):递归开销树的深度以及保存树节点的列表res
"""
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)
        res = []
        inorder(root)
        if not res:
            return 
        dummynode = TreeNode(-1)
        cur = dummynode
        for node in res:
            node.left = node.right = None
            cur.right = node
            cur = node
        return dummynode.right

"""
只保存上个节点。我们知道在中序遍历的时候， 我们每访问根节点的时候上一个访问的节点是左子树的右节点
"""
class Solution(object):
    def increasingBST(self, root):
        dummynode = TreeNode(-1)
        prev = dummynode
        self.inorder(root)
        return dummynode.right

    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        root.left = None
        prev.right = root
        prev = root
        inorder(root.right)
    

