from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort each word in the list using ASCII value
        # take the index of each word in the unchanged list 
        # map it to another list of buckets 

        keys = []      
        buckets = []   

        for word in strs:
            sig = ''.join(sorted(word))  

            if sig in keys:               
                idx = keys.index(sig)     
                buckets[idx].append(word)
            else:
                keys.append(sig)          
                buckets.append([word])    
        
        return buckets
                
