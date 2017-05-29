starred = ""
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
	else:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     / \     "
		print "|             "
		print "The noose tightens around your neck"
		print "GAME OVER!"

def read_input():
	print("Your guess? (1 letter)")
	inp = raw_input("")
	if len(inp) > 1:
		print("Error. Type only one letter!")
		read_input()
	else:
		if inp in usedletters:
			print("\nYou already tried this letter. Try a different one!")
			read_input()
		else:
			guesses_this_far(inp)
			return inp

def repl_inp(inpt, answer):
	global starred
	global guesses
	okay = 0
	print usedletters
	print "\n"
	for x in range(0,len(answer)):
		if(answer[x] == inpt):
			starred = starred[:x] + inpt + starred[x+1:]
			answer = answer[:x] + "=" + answer[x+1:]
			okay = 1
	if okay == 0:
		guesses += 1
		hangman_graphic(guesses)
		print "\n"
	print starred
	if guesses > 5:
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
		starred = starred[:x] + "*" + starred[x+1:]

def guesses_this_far(inp):
	match = 0
	global usedletters
	for x in range(0,len(usedletters)):
		if usedletters[x] == inp:
			match = 1
	if match == 0:
		usedletters.append(inp)


print("Pregame:\nEnter the word you'd like to be guessed:")
answer = raw_input("")
starring(answer)

game(answer)