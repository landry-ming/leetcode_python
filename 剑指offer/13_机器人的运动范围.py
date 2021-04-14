```
数位和的求法：
可以求余得到所求数的个位数字
然后通过整除10求模删除个位数字， 将十进制数向右移动一位
```
def sums(x):
    s = 0
    while x != 0:
        s += x % 10
        x = x // 10
    return s

```
数位和的增量
设x的数位和为S_x, x+1的数位和为S_x+1
当x+1 % 10 ！= 0的时候， 即没有进位，则S_x+1 = S_x + 1
当有进位的时候， 末尾的9变成了十位的数字+1， 即S_x+1 = S_x - 8
s_x + 1 if (x+1) % 10 else s_x - 8
```

```
现在就可以使用深度优先遍历或者广度优先遍历的方式来遍历m行n列的表格， 并将自己走过的点加入visited中，每走到一个点都有两种走法， 向下走或者向左走
每走到一个点，我们就可以判断这个点是否超出范围， 是否已经被遍历过， 数位和是否满足要求， 来判断是否走出循环
```
### 深度优先搜索
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or (si+sj) > k  or (i, j) in visited:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1, j, si+1 if (i+1) % 10 else si-8, sj) + dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj - 8)
        
        visited = set()
        return dfs(0,0,0,0)


#### 广度优先搜索
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        quene = [(0,0,0,0)]
        visited = set()

        while quene:
            i,j,si,sj = quene.pop(0)
            if i >= m or j >= n or (si+sj) > k or (i,j) in visited:
                continue
            visited.add((i,j))

            quene.append((i+1, j, si+1 if (i+1) % 10 else si - 8, sj))
            quene.append((i, j+1, si, sj+1 if (j+1) % 10 else sj - 8))

        return len(visited)
 






        