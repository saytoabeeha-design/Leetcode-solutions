class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        for i,ch in enumerate(s):
            a = s.count(ch)
            if a == 1:
                return i
        return -1
        
            
            
        
