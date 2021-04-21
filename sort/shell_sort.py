"""
时间复杂度：
最坏时间复杂度， 即当gap=1的时候， 即插入排序，最坏时间复杂度为O(n^2)
稳定：不稳定， 可能gap1：54 92  gap2:77，77 后面的77反而会跑到前面去， 所以不稳定
"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            while i >= gap:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap = gap // 2
    return alist




if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7, 7]
    print(shell_sort(alist))


