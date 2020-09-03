arr=[1,4,20,3,10,15] 
value=int(input('entr a value'))
result=[]
for i in range(len(arr)):
  result.append(arr[i])
  while(sum(result)>value):
    result.pop(0)
  if sum(result)==value:
    print(result)
