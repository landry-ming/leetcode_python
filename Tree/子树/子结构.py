### 子树
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def issametree(A, B):
            if A and B:
                return A.val == B.val and issametree(A.left, B.left) and issametree(A.right, B.right)
            else:
                return A == B
        if not B:
            return True
        if not A:
            return Tree
        return issametree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


##子结构
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A:
                return False
            return A.val == B.val  and recur(A.left, B.left) and recur(A.right, B.right)
        
        if not B or not A:
            return False
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
