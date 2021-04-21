#### 哈希表
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hashmap = set()
        cur = head
        while cur:
            if cur not in hashmap:
                hashmap.add(cur)
                cur = cur.next
            else:
                return cur

#### 检测链表中是否有环
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:   ###如果没有头结点或者头结点没有next说明一定不含有环
            return False        
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

#### 检测链表环的入口结点
"""
设定两个指针， slow， fast均指向头结点， fast每次走两步， slow每次走一步。若不存在环， 则两种不会相遇， 换回false， 若存在环， 两指针一定会相遇。因为每走 11 轮，fast 与 slow 的间距 +1+1，fast 终会追上 slow
假设fast==slow，两指针在环中第一次相遇， 下面分析两者走的步数：
f代表快指针走的步数， s代表慢指针走的步数
f = 2s
f = s + nb  a代表从头结点到环入口的距离， b代表环的长度, f和s都走了a， f比s多走了n圈
则s = nb, f = 2nb, fast和slow指针分别走了2n, n个环的周长。

从链表头部走到环状链表路口需要走到的步数是a + nb， 此时slow已经走了nb， 再把fast节点指向头节点， 相遇时即走了a步， 走到环状链表的入口。
""""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast != slow:
            return
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow

### 时间复杂度o(n)， 空间复杂度哦o(1)


