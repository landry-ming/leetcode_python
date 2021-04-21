# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### 双链表法，建立两个链表l1, l2， 从头结点开始遍历链表， 假设链表的值小于目标值， 把该节点加入到链表1， 假设该节点的值大于等于目标值
### 把该节点的值加入到目标2， 最后链表1连链表2

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = q = ListNode(-1)
        l2 = p = ListNode(-1)
        while head:
            if head.val < x:
                q.next = head
                q = q.next
            else:
                p.next = head
                p = p.next
            head = head.next
        q.next = l2.next
        p.next = None    ### 注意这里， 一定要把最后节点的下一个节点指向None， 因为这个节点的下一个节点可能还保存这以前的指向
        return l1.next

### 交换法， 指定p, q两个指针， q指针不断往后移动， 当遇到较小的值的时候就和q指针交换值。在最开始的时候我们假设遇到小于目标值的值， 会交换两者的位置
###， p,q同时向后移动， 不影响。当遇到大值时， p停止移动， q继续移动，遇到较小值的时候会交换两者的值。

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        while q:
            if q.val < x:
                p.val, q.val = q.val, p.val
                p = p.next
            q = q.next
        return head

### 头插法， 当遇到小于x值节点， 即可插到头部
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummynode = ListNode(-1)
        dummynode.next = head
        pre = dummynode
        cur = head
        while cur:
            if cur.val < x and cur != head:
                pre.next = cur.next
                cur.next = dummynode.next
                dummynode.next = cur
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return dummynode.next




                

        
                