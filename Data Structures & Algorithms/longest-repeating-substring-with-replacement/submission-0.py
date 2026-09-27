class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        mx_f=0
        mp={}
        mx_l=0
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            mx_f=max(mx_f,mp[s[right]])
            while (right-left+1)-mx_f>k:
                mp[s[left]]=mp.get(s[left],0)-1
                left+=1
            mx_l=max(mx_l,right-left+1)
        return mx_l