def knapsack(values, weights, k, i=0):
    if i == len(values):
        return 0
    elif k < 0:
        return float('-inf')
    else:
        return max(values[i]+knapsack(values, weights, k - weights[i], i+1), knapsack(values, weights, k, i+1))
    

values = [2,4,7,3,1]
weights = [3,1,4,6,3]

print(knapsack(values,weights,20))