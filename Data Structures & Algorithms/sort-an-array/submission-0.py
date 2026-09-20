class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(num:List[int]):
            if len(num)<=1:
                return num
            mid=len(num)//2
            res=[]
            left=merge_sort(num[mid:])
            right=merge_sort(num[:mid])
            i=0
            j=0
            while i< len(left) and j< len(right):
                if left[i]<= right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            while i<len(left):
                res.append(left[i])
                i+=1
            while j< len(right):
                res.append(right[j])
                j+=1
            return res
        return merge_sort(nums)