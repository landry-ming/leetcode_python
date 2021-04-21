class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        def dfs(root, path, res, target):
            if not root:
                return
            if not root.left and not root.right and target == root.val:
                path.append(root.val)
                res.append(path[:])
                path.pop()  
            path.append(root.val)
            dfs(root.left, path, res, target-root.val)
            path.pop()                                     ### 这里和257不同的是， path是一个列表，在dfs(root.left)的时候就已经发生了变化，不
            path.append(root.val)                          ## 像257的字符串， +=的时候回给dfs的path形成新的字符串
            dfs(root.right, path, res, target-root.val)
            path.pop()
            return res
        path = []
        res = []
        dfs(root, path, res, target)
        return res
        

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        def dfs(root, path, res, target):
            if not root:
                return
            if not root.left and not root.right and target == root.val:
                path.append(root.val)
                res.append(path[:]) 
            dfs(root.left, path+[root.val], res, target-root.val)                      
            dfs(root.right, path+[root.val], res, target-root.val)
            return res
        path = []
        res = []
        dfs(root, path, res, target)
        return res

时间复杂度 O(N) ： N 为二叉树的节点数，先序遍历需要遍历所有节点。
空间复杂度 O(N) ： 最差情况下，即树退化为链表时，path 存储所有树节点，使用 O(N)额外空间。

