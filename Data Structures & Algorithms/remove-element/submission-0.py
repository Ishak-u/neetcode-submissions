class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lis=[]
        for i in nums:
            if i==val:
                continue    
            lis.append(i)
        for i in range(len(lis)):
            nums[i]=lis[i]
        return len(lis)