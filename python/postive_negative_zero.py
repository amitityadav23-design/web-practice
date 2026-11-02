def postive_negative_zero(a):
 if a>0:
    return "postive"
 elif a<0:
    return "negative"
 else:
    return"zero"
x=postive_negative_zero(int(input("enter the number")))
print(x)