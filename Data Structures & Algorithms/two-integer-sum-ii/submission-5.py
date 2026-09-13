class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen=set()
        seen2=set()
        a=[-1,-1]
        n=len(numbers)

        for i in range(n):
            if numbers[i] in seen:
                seen2.add(numbers[i])
            else: 
                seen.add(numbers[i])


        for i in range(n):
            temp=target-numbers[i]
            seen.remove(numbers[i])
            if temp in seen:    
                a[0]=i+1
                for j in range(i,n):
                    if temp==numbers[j]:
                        a[1]=j+1
                        return a
            seen.add(numbers[i])            
            if temp in seen2:  
                a[0]=i+1          
                for j in range(i+1,n):
                    if temp==numbers[j]:
                        a[1]=j+1
                        return a

         
        

        