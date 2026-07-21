class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] 
        for ch in nums: 
            ans.append(ch)

        result = ans + nums 
        return result
        

    
