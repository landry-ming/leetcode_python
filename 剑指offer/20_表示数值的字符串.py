```
Created on 20210413
@author: minglang

可以把这道题看作回溯法， 但需要解决一下问题
第一， 需要建立一个列表来判断该字符有没有被选过， 如果没有，可以选择
第二， 需要进行剪枝， 即假设字符中有相同字母， 在同一层选择两个字母是没有去别的
剪枝的条件为：i > 0 and s[i] == s[i-1] and not seen[i-1], 即需要该字母拥有
前字母， 且该字母和前字母相等， 且前字母没有被选择
剪枝的前提条件是需要排序， 对字符串的排序需要将其转化成列表


```


class Solution:
    def permutation(self, s: str) -> List[str]:

        def dfs(s, path, res, seen):
            if len(path) == len(s):
                res.append(path)
                return

            for i in range(len(s)):
            
                if i > 0 and s[i] == s[i-1] and not seen[i-1]:
                    continue
                
                if not seen[i]:
                    path += s[i]
                    seen[i] = True
                    dfs(s, path, res, seen)
                    seen[i] = False
                    path = path[:-1]
        
        l = list(s)
        l.sort()
        s = ''.join(l)
            
        
        seen = [False for _ in range(len(s))]
        path = ''
        res = []
        dfs(s, path, res, seen)
        return res


