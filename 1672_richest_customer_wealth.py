class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        max_wealth = 0
        for cus in accounts:
            wealth = 0
            for money in cus:
                wealth += money 
                if wealth >= max_wealth:
                    max_wealth = wealth 

        return max_wealth
                    

        
                
        
