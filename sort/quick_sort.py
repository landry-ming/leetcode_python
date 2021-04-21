'''
时间复杂度：
最优时间复杂度：每次遍历是， 需要让左从最左边， 右指针从最右边走到主元的位置汇合， 那么这个过程就是o(n)。这个过程要执行多少次呢， 假设每次主元每次都把
                数组分成两部分， 则需要执行log(n)次， 即o(nlogn)
最坏时间复杂度：假设主元每次都把数组划分为一部分， 即主元的位置在最前面或者最后面， 则最坏时间复杂度是O(n^2)
稳定性：不稳定
'''

def quick_sort(alist):
    def quick_helper(alist, start, end):
        if start >= end:
            return 
        
        piovt = start
        left = start + 1
        right = end

        while left <= right:
            if alist[left] > alist[piovt] and alist[right] < alist[piovt]:
                alist[left], alist[right] = alist[right], alist[left]
            
            elif alist[left] <= alist[piovt]:
                left += 1

            elif alist[right] >= alist[piovt]:
                right -= 1

        alist[piovt], alist[right] = alist[right], alist[piovt]

        quick_helper(alist, start, right-1)
        quick_helper(alist, right+1, end)
    
    quick_helper(alist, 0, len(alist)-1)
    return alist

if __name__ == "__main__":
    alist = [1, 4, 2, 5, 3, 6, 8, 7, 7]
    print(quick_sort(alist))

