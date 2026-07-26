class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for sentence in sentences :
            word = sentence.split()
            length = len(word)
            if length > maximum:
                maximum = length 
        return maximum 
                
            
                
            
            
        
