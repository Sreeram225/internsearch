list1=[9,8,2,4,6,7,0 ,1,9,6,3,7]
for i in range(0,len(list1)):
  for j in range(i+1,len(list1)):
    if (list1[i]>list1[j]):
      temp=list1[i]
      list1[i]=list1[j]
      list1[j]=temp
if list1[0]==0:
  temp=list1[0]
  list1[0]=list1[1]
  list1[1]=temp
print(list1)
