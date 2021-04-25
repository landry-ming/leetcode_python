class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = "([{"
        right = ")]}"
        for char in s:
            if char in left:
                stack.append(char)
            if char in right:
                if not stack:
                    return False
                elif left.index(stack[-1]) == right.index(char):
                    stack.pop()
                else:
                    return False
        return stack == []


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        adict = {"(":")", "[":"]", "{":"}"}
        for char in s:
            if char in adict:
                stack.append(char)
            else:
                if stack and char == adict[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack == []


            
