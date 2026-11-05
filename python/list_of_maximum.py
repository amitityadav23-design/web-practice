def maximum(lst, n):
    if n==1:
        return lst[0]
    return max (lst[n-1],maximum(lst, n-1))
print(maximum([10,50,30,20],4))


