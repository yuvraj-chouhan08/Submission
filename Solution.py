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
        
l1=list(map(int,input('Enter the elements of list separated by space: ').split()))
tar=int(input('Enter the Target: '))
sol=Solution(l1,tar)
n1=sol.comb_sum(l1,tar)
print('First Combination For',tar,':',n1)
n2=sol.flatten(n1)
print("Merge Into a single Array :",n2)
n3=sol.comb2(n2)
print("Second Combination For", tar*2,":",n3)

#Sample input
# Enter the elements of list separated by space: 10 20 30 40 50 60 70 80 90 100
# Enter the Target: 150

# #Output
# First Combination For 150 : [[50, 100], [60, 90], [70, 80]]
# Merge Into a single Array : [50, 60, 70, 80, 90, 100]
# Second Combination For 300 : [[50, 60, 90, 100], [50, 70, 80, 100], [60, 70, 80, 90]]
        
            
        
            
    
