# -*- coding: utf-8 -*-
import random

boys = ["Morris", "Prajay", "Moggins", "Joe", "Bracken", "Dan Jones", "Big DJ", "Danny", "Danny Stevens",
"Boswell", "Joe Boswell", "Boozewell", "Zantow", "Max"]


characters = ["Emily", "Zak", "Sharif", "Peter Kingston", "Peter", "Zakour al-Farisi",
"Miss Kingston", "Zak al-Farisi", "Aisha", "Jamal", "Sahara"]



print boys[1]

def Randomize():
	newtext = ''
	with open("/Users/Prajay/Programming/MBULF/texts/Sarah Morgan- In The Sheik's Marriage Bed.txt") as f:
			text = f.readlines() # This will be the whole text.
			for line in text:
				for character in characters:
					if character in line:
						newtext = newtext + line.replace(character, random.choice(list(boys)))
						
	file = open("testfile.txt", "w") 
	file.write(newtext)
	file.close()					


Randomize()
