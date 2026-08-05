class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1    
        sortdic=dict(sorted(dic.items(), key= lambda a:a[1], reverse =True) )

        print(sortdic)

     
        print(type(sortdic))
        top=list(sortdic)[:k]
        return top