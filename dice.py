#Python 3.7
# from random import randint as ri
from secrets import randbelow
from sys import argv
from os.path import isfile

def mkp(w=6,c=1):
	res = []
	for i in range(w):
		nums = []
		for j in range(5):
			for k in range(c):
				# n = ri(1,6)
				n = randbelow(6)+1
			nums.append(n)
		wn = int("".join([str(a) for a in nums]))
		res.append(words.get(wn))
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
