class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=nums[0]
        count=1
        for i in range(1,len(nums)):
            x=nums[i]
            if res==x:
                count+=1
            else:
                count-=1
                if count ==0:
                    count+=1
                    res=x
        return res