#### 树的结构以及BFS, DFS的递归以及迭代实现
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_element(self, node_val):
        node = Node(node_val)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            else:
                cur.left = node
                return
            if cur.right:
                queue.append(cur.right)
            else:
                cur.right = node
                return

    def BFS(self):
        if not self.root:
            return []
        res = []
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res
    
    def dfs_preorder(self):
        def pre_helper(root):
            if not root:
                return
            res.append(root.val)
            pre_helper(root.left)
            pre_helper(root.right)
        res = []
        pre_helper(self.root)
        return res
    
    def dfs_inorder(self):
        def in_helper(root):
            if not root:
                return
            in_helper(root.left)
            res.append(root.val)
            in_helper(root.right)
        res = []
        in_helper(self.root)
        return res
    
    def dfs_postorder(self):
        def post_helper(root):
            if not root:
                return 
            post_helper(root.left)
            post_helper(root.right)
            res.append(root.val)
        res = []
        post_helper(self.root)
        return res

    ##### 迭代实现
    def preorder(self):
        if not self.root:
            return []
        
        stack = [self.root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res  

    def postorder(self):
        if not self.root:
            return []

        stack = [self.root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]
    
    def inorder(self):
        if not self.root:
            return []
        
        cur = self.root
        stack = []
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res        
            
    


a = Tree()
a.add_element(1)
a.add_element(2)
a.add_element(3)
a.add_element(4)
a.add_element(5)
a.add_element(6)
a.add_element(7)
# print(a.BFS())
# print(a.dfs_preorder())
print(a.dfs_inorder())
# print(a.dfs_postorder())
# print(a.preorder())
# print(a.postorder())
print(a.inorder())

