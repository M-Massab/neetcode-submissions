class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
           
        res = []
        nums.sort()  # Step 1: Sort the array
    
        for i in range(len(nums)):
        # Early exit: If the current number is greater than 0, 
        # it's impossible to sum to 0 with subsequent numbers.
            if nums[i] > 0:
                break
            
        # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
        # Two-pointer initialization
            left, right = i + 1, len(nums) - 1
        
            while left < right:
                total = nums[i] + nums[left] + nums[right]
            
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                
                # Move pointers and skip duplicates to avoid repetitive triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Sum is too small, increase it
                else:
                    right -= 1 # Sum is too large, decrease it
                
        return res
