class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for st in stones:
            if st in jewels :
                ans += 1 
        return ans 
                 
        
        
        
