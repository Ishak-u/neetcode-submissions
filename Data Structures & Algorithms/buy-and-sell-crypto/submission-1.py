class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left=0
        sm=prices[0]
        for right in prices:
            left=max(left,right-sm)
            sm=min(sm,right)
        return left