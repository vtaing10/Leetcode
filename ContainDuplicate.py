class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        # dupSet = {}, if i use {}, i create an empty dictionary (not a set).  
        dupSet = set() #this will allow me to .add() more items in it later (creates an empty set)
        
        for i in nums:
            if i in dupSet:
                return True
            dupSet.add(i)
        return False
