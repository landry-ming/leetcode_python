"""
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

假设当船的运载能力是x_ans时， 我们可以运输完成所有的包裹， 那么当运输能力大于x_ans时我们同样可以在D天内完成。这样一来，我们就可以得出， 存在
运输能力的下限， 即x_ans, 我们可以通过二分法来找到ans

包括不能分解， 每次最小运输最大的那个包裹， 最大运输所有包裹的总和。我们需要的是数组中的左边界， 即需要去通过二分法的右边界去卡出左边界
当运输能力是x时， 需要天数为day， 当day <= D时，说明我们可以运输更少， 即right=中间值。 否则left=中间值+1
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            need = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need <= D:
                right = mid
            else:
                left = mid+1
        return left
