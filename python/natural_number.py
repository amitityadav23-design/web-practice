def sum(a):
 if(a==0):
   return
 print(a)
 sum(a-1)
 print(a)
sum(5)