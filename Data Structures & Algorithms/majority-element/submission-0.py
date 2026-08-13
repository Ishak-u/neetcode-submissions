class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        res = count=0
        for i in nums:
            dic[i]=dic.get(i,0)+1
            if count < dic[i]:
                res=i
                count = dic[i]
        return res