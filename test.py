from sortedcontainers import SortedList


def maxSumSubmatrix(matrix, k):
    ans = float("-inf")
    m = len(matrix)
    n = len(matrix[0]) if matrix else 0

    for i in range(m):   # 枚举上边界
        total = [0] * n
        for j in range(i, m):   # 枚举下边界
            for c in range(n):
                total[c] += matrix[j][c]   # 更新每列的元素和
            
            totalSet = SortedList([0])
            s = 0
            for v in total:
                s += v
                lb = totalSet.bisect_left(s - k)
                if lb != len(totalSet):
                    ans = max(ans, s - totalSet[lb])
                totalSet.add(s)

    return ans

matrix = [[1,0,1],[0,-2,3]]
a = maxSumSubmatrix(matrix, 2)
print(a)