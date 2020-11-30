numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
set1=set()
set2=set()
intersection_set=set()
union_set=set()
for i in numbers1:
    set1.add(i)
for i in numbers2:
    set2.add(i)
for i in set1:
    if i in set2:
        intersection_set.add(i)
for i in set1:
    union_set.add(i)
for i in set2:
    union_set.add(i)
print(set1)
print(set2)
print(intersection_set)
print(union_set)