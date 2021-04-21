# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    from collections import deque
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        q = deque()
        q.append(tree)
        res = []

        while q:
            head = ListNode(0)
            cur = head

            for _ in range(len(q)):
                node = q.popleft()
                cur.next = ListNode(node.val)
                cur = cur.next

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(head.next)
        return res          
        
    
            
            
