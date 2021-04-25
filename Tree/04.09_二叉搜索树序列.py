class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        
        def helper(root, queue, path, res):
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if len(queue) == 0:
                res.append(temp+path)]
            
            for i, next_root in enumerate(queue):
                next_queue = queue[:i] + queue[i+1:]
                path.append(next_root.val)
                helper(next_root, queue, path, res)
            
