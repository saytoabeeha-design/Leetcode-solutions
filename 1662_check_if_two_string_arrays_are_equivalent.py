class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ""
        b = ""
        for st in word1:
            a += st
        for st in word2:
            b += st 
        return a == b
            
        
            
            
        
