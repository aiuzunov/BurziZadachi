#Strawberries - Александър Узунов
healthystraws = 0
decayed = []
counter = 1
counter2 = 0
counter3 = 0
inputdata = input("Въведете редове, колони и дни\n").split()
rows = int(inputdata[0])
columns = int(inputdata[1])
days = int(inputdata[2])
strawberry1 = [0, 0]
strawberry2 = [0, 0]
strawberry1 = input("Въведете местоположението на първата ягодка -> ред колона\n").split()
strawberry2 = input("Въведете местоположението на втората ягодка -> ред колона\n").split()

row1 = int(strawberry1[0])-1
col1 = int(strawberry1[1])-1
row2 = int(strawberry2[0])-1
col2 = int(strawberry2[1])-1

map = [['o' for x in range(columns)] for y in range(rows)]
map[row1][col1] = 'x'
map[row2][col2] = 'x'

def decay(x, y):
	if x < rows-1:
		if map[x+1][y] == 'o':
			map[x+1][y] = 'x'
	if x > 0:
		if map[x-1][y] == 'o':
			map[x-1][y] = 'x'
	if y < columns-1:
		if map[x][y+1] == 'o':
			map[x][y+1] = 'x'
	if y > 0:
		if map[x][y-1] == 'o':
			map[x][y-1] = 'x'
while counter <= days:
	for row in range(rows):
		for column in range(columns):
			if map[row][column] == 'x':
				decayed.append(row)
				decayed.append(column)
	while counter2 < len(decayed)/2:
		decay(decayed[counter3], decayed[counter3+1])
		counter2 += 1
		counter3 += 2
	
	counter += 1
	
for row in range(rows):
	for column in range(columns):
		if map[row][column] == 'o':
			healthystraws += 1

#for row in reversed(range(rows)):
	#print(map[row])
#print("Where: ")
#print("x - Decayed Strawberries")
#print("o - Healthy Strawberries")
print("{:d}".format(healthystraws))
