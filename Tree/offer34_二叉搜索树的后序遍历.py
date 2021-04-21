"""
后序遍历：左子树 + 右子树 + 根节点
二叉搜索树：左子树所有节点的值<根节点， 右子树所有节点的值>根节点，其左右子树也是二叉搜索树

递归分治：
根据递归， 判断所有子树的正确性。

递归终止条件：当i>=j，说明此子树的节点数量<=1，无需判别正确性， 直接返回True

递推工作：
1. 划分左右子树， 遍历后序遍历的[i,j]的元素， 寻找第一个大于根节点的节点， 索引为m， 此时左右子树的区间为[i, m-1], [m, j-1], 根节点索引为j
2. 判断是否为二叉搜索树， 左子树区间[i, m-1]中的所有节点都应<postorder[j]， 而第 1.划分左右子树 步骤已经保证左子树区间的正确性，因此只需要判断右子树区间即可。
右子树区间 [m, j-1][m,j−1] 内的所有节点都应 >> postorder[j]postorder[j] 。实现方式为遍历，当遇到 \leq postorder[j]≤postorder[j] 的节点则跳出；则可通过 p = jp=j 判断是否为二叉搜索树。

返回值：
所有子树都需正确才可判定正确，因此使用 与逻辑符 \&\&&& 连接。
p = jp=j ： 判断 此树 是否正确。
recur(i, m - 1)recur(i,m−1) ： 判断 此树的左子树 是否正确。
recur(m, j - 1)recur(m,j−1) ： 判断 此树的右子树 是否正确。

"""
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def dfs(i, j):
            if i >= j:
                return True
            
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and dfs(i, m-1) and dfs(m ,j-1)
        return dfs(0, len(postorder)-1)

时间复杂度 O(N^2)： 每次调用 recur(i,j)recur(i,j) 减去一个根节点，因此递归占用 O(N)O(N) ；最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N)O(N) 。
空间复杂度 O(N) ： 最差情况下（即当树退化为链表），递归深度将达到N。

