import os 
for f in os.scandir('C:\\Users\\Vlad\\Documents\\Lab2\\Lab2'):
	if f.is_file() and f.path.split('.')[-1].lower() == 'csv':
		with open(f.path, 'r') as csvfile:
			inText = [line.split(',') for line in csvfile]
