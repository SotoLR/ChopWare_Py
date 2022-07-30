#Python 3.7
from secrets import randbelow
from sys import argv
from os.path import isfile

# w is the amount of words in the passphrase
def mkp(w=6):
	res = []
	for i in range(w):
		#generate a number that is 5 digits long and every digit is between 1 and 6 inclusive
		#the generated number coincides with a wordlist index
		word_key = int("".join([str(randbelow(6)+1) for _ in range(5)]))
		res.append(words.get(word_key))
	return res

words = {}

wordlist="beale.wordlist.txt"

if len(argv) > 1:
	wordlist = argv[1]

if not isfile(wordlist):
	print("========================================================================")
	print(f"| Wordlist with name '{wordlist}' not found. Defaulting to Beale Wordlist... |")
	print("========================================================================")
	wordlist="beale.wordlist.txt"

with open(wordlist, "r") as f:
	#words = [ln.strip().split("\t") for ln in f.readlines()]
	for line in f:
		line = line.rstrip().split("\t")
		#print(line)
		words[int(line[0])]=line[1]

for i in range(10):
	r = mkp()
	print(' '.join(r))
	print(f"\t{''.join(r)}")

"""
http://world.std.com/~reinhold/diceware.html
	Optional stuff you don't really need to know TODO: add the option to use this stuff
http://world.std.com/%7Ereinhold/dicewarekit.html
http://world.std.com/%7Ereinhold/dicewarefaq.html#memory
"""
