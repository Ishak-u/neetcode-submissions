class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        win_s=0
        count=0
        for right in range(len(arr)):
            win_s+=arr[right]
            if right-left+1 > k:
                win_s-=arr[left]
                left+=1
            win_size =right-left+1
            if win_size == k and win_s >= threshold*k:
                count+=1
        return count