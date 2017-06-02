import os
import random
import re

starred = ""
answer = ""
error = ""
usedletters = []

guesses = 0

def hangman_graphic(guesses):
	
	if guesses == 0:
		print "________      "
		print "|      |      "
		print "|             "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 1:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 2:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /       "
		print "|             "
		print "|             "
	elif guesses == 3:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|      "
		print "|             "
		print "|             "
	elif guesses == 4:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|             "
		print "|             "
	elif guesses == 5:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     /       "
		print "|             "
	elif guesses == 6:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     / \     "
		print "|             "
		print "The noose tightens around your neck"
		print "GAME OVER!"
		print "The word was: \n 	" + answer
		raise SystemExit



def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
    	if random.randrange(num + 2) or not re.match("^[a-zA-Z]*$", aline): continue
    	line = aline
    line = line[:-1]
    return line

def return_r_line():
	with open('words.txt','r') as f:
		return random_line(f)

def starring(answer):
	global starred
	for x in range(0,len(answer)):
		if(answer[x] == " "):
			starred = starred[:x] + " " + starred[x+1:]
		else:
			starred = starred[:x] + "*" + starred[x+1:]

def allowed_c(nput):

	if nput in allowed_chars:
		return 1
	else:
		return 0

def inputcheck(inp):
	inp = inp.lower()
	return inp

def inp_len(inp):
	if len(inp) > 1:
		return 1
	else:
		return 0

def printused():

	global usedletters

	return ', '.join(usedletters)

def guesses_this_far(inp):
	
	global usedletters
	for x in range(0,len(usedletters)):
		if usedletters[x] == inp:
			return 1
	return 0

def repl_inp(nput, answer):
	global starred
	global guesses

	okay = 0

	for x in range(0,len(answer)):
		if(answer[x] == nput):
			starred = starred[:x] + nput + starred[x+1:]
			answer = answer[:x] + "=" + answer[x+1:]
			okay = 1
	if okay == 0:
		guesses += 1

def guessed():
	global starred
	nr_star = 0
	for x in range(0,len(starred)):
		if starred[x] == "*":
			nr_star += 1
	if nr_star == 0:
		return True
	else:
		return False

def read_input():

	global guesses
	global usedletters
	global error

	print("Your guess? (1 letter)")
	r_inp = ""
	r_inp = raw_input("")
	inp = inputcheck(r_inp)
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if guesses_this_far(inp) == 1:
		error = "This char has already been used"
		guesses -= 1
	else:
		usedletters.append(inp)
		return inp

def win():

	global guesses

	os.system('cls' if os.name == 'nt' else 'clear')
	hangman_graphic(guesses)
	print printused()
	print "\nCongrats! You guessed it! The word was: \n 	" + answer

def gamemode(r_answer1):
	print "Would you like to put in a word to be guessed, or should I give you a random word?"
	print "1) - Randomize it!"
	print "2) - Let me choose"

	reply = int(raw_input(""))
	if reply == 1:
		r_answer1 = return_r_line()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print "Input the word you'd like to be guessed:"
		r_answer1 = raw_input("")

	return r_answer1

def game(answer):

	global error

	while guessed() == False:
		char_in = ""
		char_in = read_input()
		repl_inp(char_in, answer)
		
		hangman_graphic(guesses)
		print printused()
		print error
		error = ""
		print starred
	win()

r_answer = ""
r_answer = gamemode(r_answer)


answer = inputcheck(r_answer)
os.system('cls' if os.name == 'nt' else 'clear')


starring(answer)

game(answer)
