class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        mn=float("inf")
        for right in range(len(nums)):
            sum+=nums[right]
            while sum >=target:
                l=right-left+1
                mn=min(l,mn)
                sum-=nums[left]
                left+=1
        if mn== float("inf"):
            return 0
        return mn