'''
时间复杂度：最坏最优都是nlogn
首先要不断的把列表分成两份， 这样的操作是logn， 然后要把分割后的数组分割遍历， 挨个比对， 这样的操作就是O(N)
算法是稳定的

'''

def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left_index = 0
    right_index = 0
    res = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1
    res += left[left_index:]
    res += right[right_index:]
    return res

if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7, 7]
    print(merge_sort(alist))