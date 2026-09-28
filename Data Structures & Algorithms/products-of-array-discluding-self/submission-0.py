class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0] * n 
        perf=[0] * n
        suf=[0] * n
        
        perf[0] = suf[n-1] = 1
        for i in range(1,n):
            perf[i]=nums[i-1] * perf[i-1]
        for i in range(n-2,-1,-1):
            suf[i]= nums[i+1] * suf[i+1]
        for i in range(n):
            res[i] = perf[i] * suf[i]
        return res