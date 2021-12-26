import random

def main():
	
	randomNumber=random.randint(1,100)
	print "Guess a number between 1 nad 100."
	found=False

	while not found:
		userGuess=input("Your Guess:")
		if userGuess==randomNumber:
			print "Bulls eye!"
			found=True

		elif userGuess > randomNumber:
			print "Guess lower."
		else:
			print "Guess Higher."


if __name__ == '__main__':
	main()