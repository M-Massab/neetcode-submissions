class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dnums=set()
        for i in nums:
            if i in dnums:
                return True
            else:
                dnums.add(i)
        return False            
        