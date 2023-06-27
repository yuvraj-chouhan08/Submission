Submission for the Following Task:
1 . Given an array of integers and a target value, you must determine which two integers' sum
equals the target and return a 2D array. Then merge the array into a single array with sorting (
ascending ) order, in the next step double the target value and find again the combination of
digits (can be multiple digits ) that are equal to the double targeted value and returned into a 2D
array.
Sample Input : [1, 3, 2, 2, -4, -6, -2, 8];
Target Value = 4,
Output: First Combination For “4” : [ [1,3],[2,2],[-4,8],[-6,2] ];

Merge Into a single Array : [-6,-4,1,2,2,2,3,8];
Second Combination For “8” : [ [ 1,3,2,2], [8,-4,2,2],....,[n,n,n,n] ]

The approach in this solution uses the combinations function from the itertools module to generate all possible combinations of elements from the list. 
The code then checks for pairs whose sum is equal to the target value and stores them in the c2 list.
The flatten method flattens the nested list list into a single list and sorts it in ascending order.
The comb2 method generates combinations from the flattened list and checks for combinations whose sum is equal to the double of the target value, t2.
