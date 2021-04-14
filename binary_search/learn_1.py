# ```
# 一般二分查找的时间复杂度为logn
# 二分法一般在已经排好序的list里才可以使用
# 难度在于边界条件，边界条件很容易出错
# ```

##### 迭代方法

def binary_search1(alist, target):
    left = 0
    right = len(alist) - 1
    while left < right:      ### 无等号
        mid = (left + right) // 2   ### 求左中分点, 当移动right=mid时需要判断左中分点
        if alist[mid] < target:
            left = mid + 1
        else:
            right = mid
    if alist[left] == target:
        return left
    else:
        return -1
    
def binary_search2(alist, target):
    left = 0
    right = len(alist) - 1 
    while left < right:
        mid = (left + right + 1) // 2 ### 求右中分点， 当移动left = mid的时候就需要判断右中分点， 即left+right+1 // 2
        if alist[mid] > target:
            right = mid - 1
        else:
            left = mid
    if alist[left] == target:
        return left
    else:
        return -1


#### 递归

def binary_search3(alist, left, right, target):
    if left == right:
        if alist[left] == target:
            return left
        else:
            return False

    mid = (left + right) // 2
    if alist[mid] < target:
        return binary_search3(alist, mid+1, right, target)
    else:
        return binary_search3(alist, left, mid, target)

# print(binary_search3([1,2,3,4,5,6], 0, 5, 5))








