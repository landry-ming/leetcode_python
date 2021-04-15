class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        if target % 2:
            n = (target // 2) + 2 
        else:
            n = (target // 2) + 1  #这里也需要用//, 单除会形成浮点数， 和1相加会报错


        start = 1
        sum_ = 0
        res = []
        for end in range(n):
            sum_ += end
            if sum_ == target:
                res.append(list(range(start, end+1)))
            
            while sum_ > target:
                sum_ -= start
                start += 1
                if sum_ == target:
                    res.append(list(range(start, end+1)))
        return res


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, sum_, res = 1, 2, 3, []

        while i < j:
            if sum_ == target:
                res.append(list(range(i, j+1)))
            elif sum_ >= target:
                sum_ -= i
                i += 1
            else:
                j += 1
                sum_ += j
        return res