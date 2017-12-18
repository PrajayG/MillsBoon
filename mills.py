
import random

ulf = {'Adam':'M', 'Alex M':'M', 'Anisa':'F' , 'Bertie':'M', 'Hannah':'F', 'Laura':'F', 'Nikki':'F',
 'Pete':'M', 'Robin':'M', 'Zoe':'F', 'Fiona':'F', 'Kat':'F', 'Emma R':'F',
'Flora':'F', 'Louisa':'F', 'Emma V':'F', 'Harry':'M', 'Darryl':'M', 'Prajay':'M'}


characters = {'Jason': 'M'}

def gatherText():
	with open("/Users/Prajay/Programming/MBULF/texts/Emma Darcy- A Very Stylish Affair.txt") as f:
		text = f.readlines()
		corpus = ''
		for x in range(0,100):
			corpus = corpus + text[x]
	print corpus
	print corpus.replace("Jason", "Adam")
	replacement = random.choice(list(ulf.keys()))
	print replacement
	print ulf[replacement]

gatherText()

print ulf["Adam"]




# str = "this is string example....wow!!! this is really string"
# print str.replace("is", "was")
# print str.replace("is", "was", 3)