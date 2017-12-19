
import random

ulf = {'Adam':'M', 'Alex M':'M', 'Anisa':'F' , 'Bertie':'M', 'Hannah':'F', 'Laura':'F', 'Nikki':'F',
 'Pete':'M', 'Robin':'M', 'Zoe':'F', 'Fiona':'F', 'Kat':'F', 'Emma R':'F',
'Flora':'F', 'Louisa':'F', 'Emma V':'F', 'Harry':'M', 'Darryl':'M', 'Prajay':'M'}


characters = {'Jason': 'M', 'Jason Lombard': 'M', 'Sophie Melville': 'F', 'Sophie': 'F', 'Mother': 'F', 'Sophie':'F',
	'Mr Lombard': 'M', 

}

def gatherText():
	with open("D:/Prajay/2017/Q4/in-house/mills/MillsBoon/texts/Emma Darcy- A Very Stylish Affair.txt") as f:
		text = f.readlines()
		corpus = ''
		for x in range(0,100):
			corpus = corpus + text[x]
	

	# print corpus.replace("Jason", "Adam")
	replacement = random.choice(list(ulf.keys()))
	if ulf[replacement] == 'M':
		print corpus.replace("Jason", replacement)
	else:
		print 'Nothing found' 
	print replacement
	print ulf[replacement]





def findMatch():
	ulfer = random.choice(list(ulf))
	char = random.choice(list(characters))
	if ulf[ulfer] == characters[char]:
		return ulfer + char
	else: 
		findMatch()

	

match = findMatch()
print match