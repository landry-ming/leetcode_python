"""
思想：
假设数组的第一个数是有序的， 然后将数组的四个数插入到有序数组中去
最坏时间复杂度：n^2
最优时间复杂度：n
稳定度:稳定
"""

def insert_sort1(alist):
    n = len(alist)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break
    return alist



def insert_sort2(alist):
    n = len(alist)

    for i in range(1, n):
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist


if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7, 7]
    print(insert_sort2(alist))