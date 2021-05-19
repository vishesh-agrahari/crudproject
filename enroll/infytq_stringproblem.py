str= input("enter string: ")
flag =False
str1 = set()
for i in str:
    if i.isdigit():
        str1.add(i)
if len(str1)!=0:
   b = sorted(str1,reverse=True)
   l1= int("".join(b))
   if l1%2==0:
       flag = True
if flag==True:
    print(l1)
else:
    print("-1")
