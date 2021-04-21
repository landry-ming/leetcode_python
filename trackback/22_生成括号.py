### 暴力法， 生成2n个括号， 去检查生成的括号是否符合规则
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n, path, res):
            if len(path) == 2*n:
                if self.valid(path):
                    res.append(''.join(path[:]))
                return
            
            path.append("(")
            generate(n, path, res)
            path.pop()
            path.append(")")
            generate(n, path, res)
            path.pop()
        
        path = []
        res = []
        generate(n, path, res)
        return res

    
    def valid(self, A):
        count = 0
        for s in A:
            if s == "(":
                count += 1
            elif s == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0

## 剪枝， 每次先生成左括号， 记录生成左括号的数量l， 且l<=n， 然后生成右括号， 且右括号数量要小于等于左括号
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n, path, res, l, r):
            if len(path) == 2*n:
                res.append(''.join(path))
                return
            if l < n:
                path.append("(")
                backtrack(n, path, res, l+1, r)
                path.pop()

            if r < l:
                path.append(")")
                backtrack(n, path, res, l ,r+1)
                path.pop()
        path = []
        res = []
        backtrack(n, path, res, 0, 0)
        return res                
