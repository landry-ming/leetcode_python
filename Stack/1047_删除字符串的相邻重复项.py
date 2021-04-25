""""
可以使用栈，遍历每一个字符， 遇到栈为空或者字符不等于栈的最后一个字符， 则把该字符入栈
遇到相等的情况， 则把它出栈。
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if not stack or s != stack[-1]:
                stack.append(s)
            else:
                stack.pop()

        return "".join(stack)

        