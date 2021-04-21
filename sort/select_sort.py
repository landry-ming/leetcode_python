"""
思想
每次遍历数组， 从数组中选择最小的数放在列表里的位置

最优时间复杂度：n^2
稳定的算法
"""
def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist

if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7, 7]
    print(select_sort(alist))

        
        