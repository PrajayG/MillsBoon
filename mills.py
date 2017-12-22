
import random

ulf = { 'Gus':'F', 'Robin':'M'}


characters = {'Zak': 'M',  'Emily': 'F'}



	
def gatherText():
	with open("D:/Prajay/2017/Q4/in-house/mills/MillsBoon/texts/shiek/chapter11.txt") as f:
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

	


gatherText()