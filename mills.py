
import random

ulf = {'Adam':'M', 'Alex':'M', 'Anisa':'F', 'Bertie':'M', 'Hannah':'F', 'Laura':'F', 'Nikki':'F',
 'Pete':'M', 'Robin':'M', 'Zoe':'F', 'Fiona':'F', 'Kat':'F', 'EmRob':'F',
'Flora':'F', 'Louisa':'F', 'Emma':'F', 'Harry':'M', 'Darryl':'M', 'Prajay':'M'}


characters = {'Zak': 'M', 'Sharif': 'M', 'Emily': 'F'}



	
def gatherText():
	with open("D:/Prajay/2017/Q4/in-house/mills/MillsBoon/texts/shiek/chapter1.txt") as f:
		text = f.read() # This will be the whole text.
		match = findMatch()
		text = text.replace(match[1], match[0])

		text = text.replace(match[3], match[2])
		print text
		print match
		
	


def findMatch():
	ulfer = random.choice(list(ulf))
	char = random.choice(list(characters))
	ulfer2 = random.choice(list(ulf))
	char2 = random.choice(list(characters))
	doublecheck = [ulfer, char]
	if (ulfer2 == doublecheck[0]) or (char2 == doublecheck[1]):
		return findMatch()
	replacements = []
	if (ulf[ulfer] == characters[char]) and (ulf[ulfer2] == characters[char2]):
		replacements.append(ulfer)
		replacements.append(char)
		replacements.append(ulfer2)
		replacements.append(char2)
		print 'Success!'
		return replacements	
	else: 
		print 'Error: same sex found'
		return findMatch()
# Consider returning more than one match in the list that comes back?
	


gatherText()