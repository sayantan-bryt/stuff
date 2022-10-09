name = 'Harrison'
guess = raw_input("So I'm thinking of a name. Try and guess it: ")
pos = 0

while guess != name and pos < len(name):
	print("Nope, thant's not it! Hint: letter ", end='')
	print(pos + 1,"is",name[pos] + ". ", end='')
	pos = pos + 1

if pos == len(name) and name != guess:
	print("Too bad, you couldn't get it. The name was", name + ".")
else:
	print("\nGreat, you got it in", pos + 1, "guesses!")
