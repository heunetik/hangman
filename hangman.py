import os

starred = ""
usedletters = []
guesses = 0
allowed_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','10','0']


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
		raise SystemExit

def read_input():

	global guesses

	print("Your guess? (1 letter)")
	r_inp = raw_input("")
	inp = inputcheck(r_inp)
	if len(inp) > 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		hangman_graphic(guesses)
		printused(usedletters)
		print("Error. Type only one letter!\n")
		print starred
		read_input()
	else:
		if inp in usedletters:
			#os.system('cls' if os.name == 'nt' else 'clear')
			hangman_graphic(guesses)

			print("\nYou already tried this letter. Try a different one!")
			guesses -= 1
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			hangman_graphic(guesses)
			guesses_this_far(inp)
			return inp

def inputcheck(inp):
	inp = inp.lower()
	return inp

def printused(used):
	global usedletters
	print ', '.join(usedletters)

def repl_inp(inpt, answer):
	global starred
	global guesses
	okay = 0
	print "\n"
	#print "\n"
	for x in range(0,len(answer)):
		if(answer[x] == inpt):
			starred = starred[:x] + inpt + starred[x+1:]
			answer = answer[:x] + "=" + answer[x+1:]
			okay = 1
	if okay == 0:
		guesses += 1
		os.system('cls' if os.name == 'nt' else 'clear')
		hangman_graphic(guesses)
		printused(usedletters)
		print "\n"
	print starred
	if guesses > 6:
		raise SystemExit

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

def game(answer):
	while guessed() == False:
		char_in = read_input()
		repl_inp(char_in, answer)

def starring(answer):
	global starred
	for x in range(0,len(answer)):
		if(answer[x] == " "):
			starred = starred[:x] + " " + starred[x+1:]
		else:
			starred = starred[:x] + "*" + starred[x+1:]

def guesses_this_far(inp):
	match = 0
	global usedletters
	for x in range(0,len(usedletters)):
		if usedletters[x] == inp:
			match = 1
	if match == 0:
		usedletters.append(inp)
	printused(usedletters)


print("Pregame:\nEnter the word you'd like to be guessed:")
r_answer = raw_input("")
answer = inputcheck(r_answer)
os.system('cls' if os.name == 'nt' else 'clear')
starring(answer)

game(answer)
