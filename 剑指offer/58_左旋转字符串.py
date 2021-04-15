class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        for i in range(n):
            s= "".join(list(s[1:])) + s[0]
        return s

```
字符串的切片
获取字符串s[n:]切片和字符串s[:n]切片， 使用+运算符拼接并返回即可
时间复杂度：O(N), 其中N为字符串的长度， 字符串切片函数为线性复杂度
空间复杂度O(N), 两个字符串切片的总长度为N

切片的效率最高， 无冗余操作
```
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

```
列表遍历拼接
新建一个列表res
先向res中添加第n+1位至末位的字符
再向res添加首位至第n位的字符
将res转化成字符串并返回
时间复杂度：O(N) 线性遍历s并添加， 使用线性空间
空间复杂度

每轮遍历拼接字符时， 只是向列表尾部添加一个新的字符元素， 最终拼接转化成字符串
系统仅申请一次内存
```
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        
        for i in range(n):
            res.append(s[i])
        
        return "".join(res)


```
字符串遍历拼接
时间复杂度O(N), 空间复杂度O(N)
字符串是不可变的对象， 因此每轮遍历连接字符， 都需要新建字符串， 因此， 需要申请N次内存， 效率低下。
```
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ''
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res


