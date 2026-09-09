class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        maxi=0
        seen=set(nums)
        nonrep=set()
   
       
        maxx=max(nums)
        minn=min(nums)
        
        def back(a:int)->int:
            current=1
            temp=a-1
           
            while(temp>minn):
                if temp in seen:
                    nonrep.add(temp)
                    
                    current+=1
                    temp-=1
                else: 
                    break
              
            return current

        def forward(b:int,maxx:int)->int:
            current=0
            temp=b+1
            while(temp<=maxx):
                if temp in seen:
                    nonrep.add(temp)
                    current+=1
                    temp+=1
                else: 
                    break
                     
            return current     


            



      
        for i in range(n):
            if nums[i] not in nonrep:
               
                current=0
                current=back(nums[i])
                current+=forward(nums[i],maxx)
                if current>maxi:
                    maxi=current
            nonrep.add(nums[i])        

        return maxi        
        