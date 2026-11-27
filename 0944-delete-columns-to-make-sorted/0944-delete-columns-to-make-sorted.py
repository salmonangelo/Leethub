class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        ans = 0
        for i in range(m):
            for j in range(1,n):
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    ans+=1
                    break
            
        return ans