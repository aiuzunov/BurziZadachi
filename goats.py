import itertools

goatsnum=int(input("Enter the number of goats: "))
courses=int(input("Enter the number of courses: "))
goats=[]
for i in range(goatsnum):
	goats.append(int(input("Enter the weight of goat #{} ".format(i+1))))
boatlenght=1
totalgoatweight = sum(goats)
goats.sort(reverse=True) 
finalboatweight=-1
i=0
while i < goatsnum:
	for x in itertools.permutations(goats, i):
		if sum(x)==totalgoatweight/courses:
			if(finalboatweight<sum(x)):
				finalboatweight=sum(x)
	i=i+1
print("The boat weight must be: {:d}".format(finalboatweight))
		
#print goats(itertools.permutations([1,2,3,4], boatlength))
