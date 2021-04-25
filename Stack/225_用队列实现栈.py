"""
每次使用A，B两个栈，push元素时首先将元素加入到B栈中，然后将A中的元素依次pop(0)， 再append到b中
这样b中最左边的元素就是最新添加的， 再把b交给a完成由队列完成栈！
"""
class MyStack:

    def __init__(self):
        self.A = []
        self.B = []

    def push(self, val):
        self.B.append(val)
        while self.A:
            self.B.append(self.A.pop(0))
        self.A, self.B = self.B, self.A
    
    def pop(self):
        return self.A.pop(0)

    def top(self):
        return self.A[0]

    def empty(self):
        return self.A == []

### 官方写法：
import collections
class MyStack:
    
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
    
    def push(self, val):
        self.queue2.append(val)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]
    
    def empty(self):
        return not self.queue1   ###这里记得用==[]不行
