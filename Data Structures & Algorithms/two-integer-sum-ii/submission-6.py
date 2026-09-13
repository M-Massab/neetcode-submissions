class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Maps the number value to its 1-based index
        seen_map = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            # If the complement was already seen, we found the pair!
            if complement in seen_map:
                return [seen_map[complement], i + 1]
            
            # Otherwise, save the current number and its 1-based index
            seen_map[num] = i + 1
            
        return [-1, -1]
