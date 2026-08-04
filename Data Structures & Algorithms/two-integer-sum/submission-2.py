class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndic = {num: i for i, num in enumerate(nums)}
        
        ans=[]
        for i,j in enumerate (nums):
            
            if (target-j) in ndic and i!= ndic[target-j]:
                
                ans.append(i)
                ans.append(ndic[target-j])
                return ans