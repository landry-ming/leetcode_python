"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

 
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        def dfs(start_index, path, res, s):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index, len(s)):
                if s[start_index:i+1] == s[start_index:i+1][::-1]:
                    path.append(s[start_index:i+1])
                    dfs(i+1, path, res, s)
                    path.pop()
        path = []
        res = []
        dfs(0, path, res, s)
        return res
            

"""
增加， 判断一个字符串列表中以i开始， j结尾的字符串是不是回文字符串
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            if not s:
                return False
            
            dp = [[False]*len(s) for _ in range(len(s))]
            for i in range(len(s)):
                dp[i][i] = True
            for j in range(1, len(s)):
                for i in range(j):
                    if s[i] == s[j]:
                        if j - i <= 1:
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i+1][j-1]
            return dp

        if not s:
            return []
        def dfs(start_index, path, res, s):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index, len(s)):
                if dp[start_index, i]:
                    path.append(s[start_index:i+1])
                    dfs(i+1, path, res, s)
                    path.pop()
        path = []
        res = []
        dfs(0, path, res, s)
        return res
            


                



                
