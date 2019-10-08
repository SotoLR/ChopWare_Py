from random import randint as ri
#from secrets import 

def mkp(w=6,c=1):
	res = []
	for i in range(w):
		nums = []
		for j in range(5):
			for k in range(c):
				n = ri(1,6)
			nums.append(n)
		wn = int("".join([str(a) for a in nums]))
		res.append(words.get(wn))
	return res


wordlist="beale.wordlist.txt"

words = {}

with open(wordlist, "r") as f:
	#words = [ln.strip().split("\t") for ln in f.readlines()]
	for line in f:
		line = line.rstrip().split("\t")
		#print(line)
		words[int(line[0])]=line[1]

for i in range(10):
	r = mkp()
	print(r)
	print(f"\t{''.join(r)}")

"""
http://world.std.com/~reinhold/diceware.html
	Optional stuff you don't really need to know
http://world.std.com/%7Ereinhold/dicewarekit.html
http://world.std.com/%7Ereinhold/dicewarefaq.html#memory
"""