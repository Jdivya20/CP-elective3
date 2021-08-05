# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	nth
import itertools
def limitedPowerSet(n, k):
    # Your code goes here...
    s=set(())
    a=[{}]
    for i in range(1,n+1):
        s.add(i)
    for i in range(1,len(s)+1):
        p=list(map(set,itertools.combinations(s,i)))
        for j in range(len(p)):
            if len(a)!=k:
                a.append(p[j])
            else:
                return a
print(limitedPowerSet(5, 7))