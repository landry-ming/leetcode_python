"""
生成一个栈， 去遍历这个字符串， 当栈为空时或者该字符串不等于栈顶元素时， 就把该字符以及字符的数量加入到字符串中
即[s, 1]
遇到相等元素时， 把数量加1， 当数量等于k时就可以把字符弹出。
注意生成结果时， 要把字符串从栈顶弹出， 这样顺序是ok的
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for astr in s:
            if not stack:
                stack.append([astr, 1])
            elif astr != stack[-1][0]:
                stack.append([astr, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == K:
                    stack.pop()
        res = ''
        while stack:
            cur = stack.pop(0)
            res += cur[0] * cur[1]
        return res

        #### return "".join(char * cnt for char, cnt in stack)


"""

"""