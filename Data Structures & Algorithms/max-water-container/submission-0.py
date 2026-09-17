class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        n=n-1
        i=0
        maxm=0
        print(n)
        while(i<n):
            width=n-i
            length=min(heights[i],heights[n])
            area=width*length
            if maxm<area:
                maxm=area
            if heights[i]>heights[n]:
                n=n-1
            else:
                i=i+1        
        
        
        
        
        
        return maxm 