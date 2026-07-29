class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = ""
        alph = "abcdefghijklmnopqrstuvwxyz"
        for ch in sentence:
            if ch in alph :
               if ch not in ans :
                   ans += ch
            
        return len(ans) == 26
            
            
        
        
