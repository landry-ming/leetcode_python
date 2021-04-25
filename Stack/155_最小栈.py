class MinStack:
    def __init__(self):
        self.A = []
        self.B = []

    
    def push(self, val):
        self.A.append(val)
        if not self.B or val <= self.B[-1]:   #### 这里的主要思想是A存放栈的元素， B存放一个非严格递减的元素值，当新增的元素小于等于栈B顶端的元素时， 就会把值压入到栈中。
            self.B.append(val)


    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    
    def top(self):
        if self.A:
            return self.A[-1]


    def getMin(self):
        if self.B:
            return self.B[-1]


"""
第一中方法是遇到小的再把它添加到辅助栈中， 这样子再弹出的时候也需要就是遇到和栈顶元素相同的再弹出。
也可以每次都往辅助栈里添加元素， 如果新的值比较小就append新的值， 如果新的值比较大，就append旧值。
"""

