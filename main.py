from itertools import combinations
class Solution:
    def __init__(self,List,target):
        self.List=List
        self.target=target
    def comb_sum(self,List,target):
        c1=[]
        c2=[]
        for r in range(len(self.List)+1):
            c1+=list(combinations(self.List,r))
        for i in c1:
            if len(i)==2 and sum(i)==self.target:
                c2.append(list(i))
        return c2
    def flatten(self,list):
        c3=[j for i in list for j in i]
        c3=sorted(c3)
        return c3
    def comb2(self,li):
        t2=self.target*2
        x1=[]
        x2=[]
        for r in range(len(li)+1):
            x1+=list(combinations(li,r))
        for i in x1:
            if sum(i)==t2:
                x2.append(list(i))
        return x2
l1=[1, 3, 2, 2, -4, -6, -2, 8] 
tar=4
sol=Solution(l1,tar)
n1=sol.comb_sum(l1,tar)
print('First Combination For “4” :',n1)
n2=sol.flatten(n1)
print("Merge Into a single Array :",n2)
n3=sol.comb2(n2)
print("Second Combination For “8” :",n3)

#Output
# First Combination For “4” : [[1, 3], [2, 2], [-4, 8]]
# Merge Into a single Array : [-4, 1, 2, 2, 3, 8]
# Second Combination For “8” : [[8], [-4, 1, 3, 8], [-4, 2, 2, 8], [1, 2, 2, 3]]
        
            
        
            
    
