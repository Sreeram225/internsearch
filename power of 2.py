n= int(input('enter  a number')
print(bin(n))
i=0
for x in str(bin(n)):
   if x==str(1):
       i=i+1
print(i)
if i==1:
    print('enter value is power of 2')
else:
 print('entered value is  not power of 2')
