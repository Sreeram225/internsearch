list1=[1,-2,1]
list2=[]
i=int(input())
list2=list1*i
print(list2)
cur_sum=[]
sublist=[]
total=0
for i in range(0,len(list2)+1):
  for j in range(i+1,len(list2)+1):
    sub=list2[i:j]
    sublist.append(sub)
    x=sum(sub)
    cur_sum.append(x)
print(max(cur_sum))
