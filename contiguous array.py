list1=[1, 2, 3, -2, 5]
sublist=[[]]
cur_sum=[]
dict1={}
for i in range(len(list1)+1):
  for j in range(i+1,len(list1)+1):
    sub=list1[i:j]
    sublist.append(sub)
    x=sum(sub)
    print(sub,         "sum ", x)
    cur_sum.append(x)
print("maximum contiguous array sum is ",max(cur_sum))
