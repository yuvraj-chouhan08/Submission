from itertools import combinations
                                           # combinations function from the itertools module to generate all possible combinations of elements from the list.
class Solution:
    def __init__(self,List,target):
        self.List=List
        self.target=target
    def comb_sum(self,List,target):
        c1=[]                              # c1 stores all possible combinations of elements from the list.
        c2=[]          
        for r in range(len(self.List)+1):
            c1+=list(combinations(self.List,r))
        for i in c1:
            if len(i)==2 and sum(i)==self.target:
                c2.append(list(i))        # The code then checks for pairs whose sum is equal to the target value and stores them in the c2 list
        return c2
    def flatten(self,list):
        c3=[j for i in list for j in i]   # The flatten method flattens the nested list list into a single list and sorts it in ascending order
        c3=sorted(c3)
        return c3
    def comb2(self,li):                   # The comb2 method generates combinations from the flattened list and checks for combinations whose sum is equal to the double of the target value, t2.
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


#Sample input 1
# Enter the elements of list separated by space: 
# 1 3 2 2 -6 -4 -2 8
# Enter the Target: 
# 4
# First Combination For 4 : [[1, 3], [2, 2], [-4, 8]]
# Merge Into a single Array : [-4, 1, 2, 2, 3, 8]
# Second Combination For 8 : [[8], [-4, 1, 3, 8], [-4, 2, 2, 8], [1, 2, 2, 3]]

#Sample input 2
# Enter the elements of list separated by space: 10 20 30 40 50 60 70 80 90 100
# Enter the Target: 150

# #Output
# First Combination For 150 : [[50, 100], [60, 90], [70, 80]]
# Merge Into a single Array : [50, 60, 70, 80, 90, 100]
# Second Combination For 300 : [[50, 60, 90, 100], [50, 70, 80, 100], [60, 70, 80, 90]]
        
            
        
            
    
