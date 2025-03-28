class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Hset = {} #value -> index ,  using set() creates a set and {} creates a dictionnary (key,value)
        #i is index j is value when using enumerate
        for i,j in enumerate(nums):
            difference = target - j
            if difference in Hset: #checks if difference exist in the previous iterations
                return [Hset[difference], i]
            Hset[j] =i
# [3,4,5,6] target 7
#{3->0, 4 ->1, ...}