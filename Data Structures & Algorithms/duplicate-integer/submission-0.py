class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1= set()
        for i in range(len(nums)):
            num1.add(nums[i])
        if len(nums)>len(num1):
            return True
        else:
            return False