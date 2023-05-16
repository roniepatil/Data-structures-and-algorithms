def knapsack(values, weights, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,k) in lookup:
        return lookup[(i,k)]
    if i == len(values):
        return 0
    elif k < 0:
        return float('-inf')
    else:
        lookup[(i,k)] = max(values[i]+knapsack(values,weights,k-weights[i],i+1,lookup),knapsack(values,weights,k,i+1,lookup))
        return lookup[(i,k)]

values = [2,4,7,3,1]
weights = [3,1,4,6,3]

print(knapsack(values,weights,20))