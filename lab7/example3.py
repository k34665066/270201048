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
averagelist=[]
for i in value:
	averagelist.append(int((i[0]+i[1])/2))
newlist=[]
counter=0
value=newlist
for i in range(len(books)):
	newlist.append((value1list[counter],value2list[counter],averagelist[counter]))
	counter+=1
newlist=tuple[newlist]




bookcount=0
for i in range(len(value)):
	book_dict[books[bookcount]]=value[bookcount]
	bookcount+=1
print(book_dict)