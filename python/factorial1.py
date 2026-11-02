def factorial(a):
  fact=1
  for i in range(1,a+1):
      fact*=i
  return fact
f=factorial(int(input("entr the number")))
print(f)
