class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
        
        if len(list1) == len(nums):
            return False
        
        return True
            