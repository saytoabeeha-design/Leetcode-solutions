class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        ans = 0
        while num > 0:
            digit = num % 10
            num = num // 10 
            if original % digit == 0:
                ans += 1

        return ans 
            
                
                
        
      
               
               
                
        
