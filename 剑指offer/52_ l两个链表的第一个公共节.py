# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#### 哈希指针是最简单的思路


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashtable = set()
        index1 = headA
        index2 = headB

        while index1:
            hashtable.add(index1)
            index1 = index1.next
        
        while index2:
            if index2 in hashtable:
                return index2
            index2 = index2.next
        
        return None


```
### 双指针
指针1， 2均指向两个链表的头节点
遍历两个指针， 直到走到链表的末尾。指针1走到指针的末尾， 则重新指向链表2
指针2走到指针的末尾则重新指向链表1
这样两个指针走的路为：链表1 》 none > 链表2 》 相遇节点
链表2 》 none 》 链表1 》 相遇节点
```

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        index1 = headA
        index2 = headB

        while index1 != index2:
            index1 = index1.next if index1 else headB
            index2 = index2.next if index2 else headA
        
        return index1

