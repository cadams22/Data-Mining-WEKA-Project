import csv
from string import punctuation as p


def openFeat():
	Ffile = open('features.csv', 'r')

	DictId = {}
	featList = csv.reader(Ffile, ['ID' , 'Term'])
	
	for line in featList:	
		d = termDict(line[1:])
		DictId[line[0].strip()] = d
	return DictId
		

def termDict(t):
	l = {}

	for term in t:
		term.strip()
		
		x = 2
		s = ''
		while x < len(term) and term[x] != '"':
			s = s + term[x]
			x = x + 1 
		
		s = s.strip()
		flag = False
		while x < len(term):
			if(term[x] == '"' or term[x] == ':' or term[x] == ' '):
				flag = False
				pass
			else:
				flag = True
				number = int(term[x:])
				break
			x = x + 1
		if flag:
			l[s] = number
	
	print l
	return l 	
			
def edgeNameOpen(some_file):

	DictE = {}
	EList = csv.reader(some_file)
	
	return EList			
		

def findEdgeAuthors(edgeN, some_file):
	Elist = edgeNameOpen(some_file)

	for label in Elist:
		#label[0].strip()
		if label[0] != 'id ' and int(label[0]) == edgeN:
			return [label[1].strip(), label[2].strip()]

def compare(n, tDict, some_file):
	authors = findEdgeAuthors(n,some_file)
	total = 0
	if authors is not None:
		
 		if(authors[0] in tDict and authors[1] in tDict):
			x1 = tDict[authors[0]]
			x2 = tDict[authors[1]]
			flag = False
 
			if x1 == x2:
				return True 
			return flag


	return False


def openTest():
	tfile = open('test.csv', 'r')

	DictId = {}
	testList = csv.reader(tfile)
	
	for line in testList:
		DictId[line[0]] = line[1]
	
	return DictId

testDict = openTest()
authDict = openFeat()
some_file = open('edge_names.csv','r')

counter = 0
for i in range(1,5000):
	i = compare(i, authDict,some_file)
	if i is True :
		counter+=1
