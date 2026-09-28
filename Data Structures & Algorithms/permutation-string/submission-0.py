class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        dic={}
        target={}
        for i in range(len(s1)):
            target[s1[i]]=target.get(s1[i],0)+1
        for right in range(len(s2)):
            dic[s2[right]]=dic.get(s2[right],0)+1
            if right-left+1 > len(s1):
                dic[s2[left]]-=1
                if dic[s2[left]]==0:
                    del dic[s2[left]]
                left+=1
            if right-left+1==len(s1):
                if target==dic:
                    return True
        return False