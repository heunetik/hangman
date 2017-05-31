import os

starred = ""
answer = ""
error = ""
usedletters = []
allowed_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','10','0']

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
	
	match = 0
	global usedletters
	for x in range(0,len(usedletters)):
		if usedletters[x] == inp:
			match = 1
	if match == 0:
		return 0
	else:
		return 1

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

print("Pregame:\nEnter the word you'd like to be guessed:")
r_answer = raw_input("")
answer = inputcheck(r_answer)
os.system('cls' if os.name == 'nt' else 'clear')


starring(answer)

#parsed input:
game(answer)
#os.system('cls' if os.name == 'nt' else 'clear')
