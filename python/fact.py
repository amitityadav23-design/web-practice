def fact(s):
    if (s==1):
      return 1
    return s*fact(s-1)
print(fact(10))
