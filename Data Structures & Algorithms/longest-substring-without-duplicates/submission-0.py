class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        win=set()
        mx_len=0
        for right in range(len(s)):
            while s[right]  in win:
                win.remove(s[left])
                left+=1
            win.add(s[right])
            mx_len=max(mx_len,right-left+1)
        return mx_len