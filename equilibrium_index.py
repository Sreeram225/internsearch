arr=[-1,2,-1 ]
equilibrium_index=int(len(arr)/2)
low_sum=sum(arr[:equilibrium_index])
high_sum=sum(arr[(equilibrium_index+1):])
print(low_sum)
print(high_sum)
if low_sum==high_sum:
  print('{} is an aquilibrium index'.format(equilibrium_index))
else:
  print('not an equilibrium index')
