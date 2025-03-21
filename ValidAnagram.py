class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        #need to work with counter, otherwise, a case like "cbcc" and "cbbc" would be true if working with letter sets
        sCounter ={}
        tCounter ={}
        for i in range(len(s)):
            sCounter[s[i]]= 1+ sCounter.get(s[i],0) #,0 is in case the count is 0
            tCounter[s[i]]= 1+ tCounter.get(t[i],0)
            
        return sCounter==tCounter
            
            
            
            
            
            #if 1 hashset
            #s = "ccbb"
            # t = "cbcb"
            # Hset = {c :2 . b:2} after s iteration
            # for t:
            #for char in len(t)
            #if char == key.Hset
            # reduce value
            #Hset = {c :1 , b:2}
            #end check if values = 0