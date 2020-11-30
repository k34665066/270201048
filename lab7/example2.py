books=["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDERS'S GAME"]
book_dict={}
value1list=list()
value2list=list()
sets=set()
for i in books:
	value1=len(i)
	value1list.append(value1)
	sets = set()
	for a in i:
		sets.add(a)

	value2=len(sets)
	value2list.append(value2)

value=list(zip(value1list,value2list))
print(value)
bookcount=0
for i in range(len(value)):
	book_dict[books[bookcount]]=value[bookcount]
	bookcount+=1
print(book_dict)