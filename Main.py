import os 
for f in os.scandir('C:\\Users\\Vlad\\Documents\\Lab2\\Lab2'):
	if f.is_file() and f.path.split('.')[-1].lower() == 'csv':
		with open(f.path, 'r') as csvfile:
			inText = [line.split(',') for line in csvfile.read().splitlines()]

def Create_Score(Score_list):
	Score = 12
	for elem in Score_list:
		Score_list = int(elem)

	for i in range(len(Score_list)):
		if i == 0:
			Score = 12
		elif i == 1:
			Score = 10
		elif i == 2:
			Score  = 8
		else:
			i -= 1
		max_elem = max(Score_list)
		Score_list[Score_list.index(max_elem)] = Score

Numb_of_Countries = inText[0][0]
Max_Coins = 0
del inText[0]
Countries = []
for row in inText:
	print(row)
for i in range(len(inText[1])):
	for j  in range(len(inText)):
		if i == 0:
			pass
		else:
			if int(inText[j][i]) > Max_Coins:
				Max_Coins = int(inText[j][i])

		print(inText[j][i])
print(Countries)






