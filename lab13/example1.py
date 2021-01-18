def selection_sort(list):
  if len(list)==1:
    return list
  else:
    x1=list[0]
    x=0
    for i in range(len(list)):
      if x1>=list[i]:
        x1=list[i]
        x=i
    list[0],list[x]=x1,list[0]
    return [list[0]] + selection_sort(list[1:])


print(selection_sort([4,3,1,7,2,-1,-4,5,7,8]))