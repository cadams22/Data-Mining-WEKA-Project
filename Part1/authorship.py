import csv
from string import punctuation as p


def openFeat():
	Ffile = open('features.csv', 'r')

	DictId = {}
	featList = csv.reader(Ffile, ['ID' , 'Term'])
	
	for line in featList:
		
		d = termDict(line[1:])
		DictId[line[0].strip()] = d
	#print DictId
	return DictId
		

def termDict(t):
	l = {}

	for term in t:
		term.strip()
		#print term
		
		x = 2
		s = ''
		#print term[x]
		while x < len(term) and term[x] != '"':
			#print term[x]
			s = s + term[x]
			x = x + 1 
		
		s = s.strip()
		#print s
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
		
	return l 	
			
def edgeNameOpen():
	Efile = open('edge_names.csv', 'r')

	DictE = {}
	EList = csv.reader(Efile)
	
	return EList			
		

def findEdgeAuthors(edgeN, Elist):

	for label in Elist:
		#label[0].strip()
		if label[0] != 'id ' and int(label[0]) == edgeN:
			return [label[1].strip(), label[2].strip()]

def compare(n, tDict, Elist):
	authors = findEdgeAuthors(n,Elist)
	total = 0
	if authors is not None:
		#print authors
		
		if(authors[0] in tDict and authors[1] in tDict):
			A0terms = tDict[authors[0]]
			A1terms = tDict[authors[1]]

		#print A0terms
		#print A1terms

			flag = False
 
			for x1 in A0terms:
				for x2 in A1terms:
					if x1 == x2:
						if(len(x1) > 1):
							if x1[len(x1)-1] in p: 
								print x1
								return True 
			return flag

	return False




def openTest():
	tfile = open('test.csv', 'r')

	testId = {}
	testList = csv.reader(tfile, ['id', 'coauthors'])
	count = 0
	for line in testList:
		testId[line[0]] = line[1]
	
	
	return testId


testDict = openTest()



authDict = openFeat()

some_file = open('edge_names.csv','r')
fiyul = open('submissionn.csv','a')
fiyul.write("id , coauthors\n")

counter = 5001
for i in range(5001,20001):
	i = compare(i, authDict,some_file)
	fiyul.write(str(counter) + " , " + str(int(i)) + "\n")
	counter = counter + 1
some_file.close()
fiyul.close()