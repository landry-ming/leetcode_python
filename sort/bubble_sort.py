"""
思想：
每次从第一个数开始， 然后把这个数和这个数的后面一个比较， 如果这个数大就调换位置， 一次循环后就把最大的那个数调换到了最后面。
假设列表里有n个数， 则需要n-1次循环， 才能把列表排好

最坏时间复杂度：n^2
最优时间复杂度n，假设数组的顺序是排好的， 那么第一次就没有任何两个数字的位置被调换， 定义计数变量， 假设在某次循环时， count=0， 则说明数组顺序完成， 退出循环
稳定的排序算法
"""

def bubble_sort(alist):
    n = len(alist)

    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:
            break
    return alist


if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7]
    print(bubble_sort(alist))