import csv

def format():
	f = open('answers.csv', 'r')
	fc = csv.reader(f)

	w = open('maddie.csv', 'w')

	wc = csv.writer(w)
	wc.writerow(['id ', ' friends'])
	count = 5001
	for line in fc:
		for st in line:
			for c in range(0, len(st)-1):
				if st[c] == ':':
					print (st[c+1])
					wc.writerow([count, str(st[c+1])])
					
					count = count + 1
					break
	print(count)
format()