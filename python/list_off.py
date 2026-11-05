def totale(lst,n):
     if (n==0):
        return 0
    return lst[n-1]+totale(lst, n-1)
print(totale([10,20,30],3))