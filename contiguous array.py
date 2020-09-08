list1=[1,2,3,4,5]
sublist=[[]]
for i in range(len(list1)+1):
  for j in range(i+1,len(list1)+1):
    sub=list1[i:j]
    sublist.append(sub)
    print(sub)
    x=sum(sub)
    print(x)
