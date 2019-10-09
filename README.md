# ChopWare_Py
Python version of a CLI diceware password creation tool

## How does it work?
At this point, it's very simple. The bulk of the logic occurs in the *mkp(w,c)* function, which generates a passphrase *w* words long from the data in whatever file has been saved to the *wordlist* variable. Generating each word in the passphrase requires 5 numbers between 1 and 6, each randomly generated. Modifying the *c* parameter will increase the amount of times the tool will "roll" for that number. The purpose of this is to increase randomness, but I am unsure if there is even a point in that. Or is a number generated now less random than a number generated 12 milliseconds from now? Don't know, will find out before this tool is done.

The default values for *w* and *c* are 6 and 1, respectively. You can run the function with or without parameters.

## Contents:
dice.py - *Da Code*

### Wordlists
  
beale.wordlist.txt - Word list created by Alan Beale. Replaces words in diceware.wordlist.txt that might be harder to remember for people who were not born or live in the US (e.g. ncaa, idaho)

diceware.wordlist.txt - General wordlist

long_wordlist.txt - Uses longer words

med_wordlist.txt - Uses medium-size words

short_wordlist.txt - Uses short words

sp.txt - I honestly can't remember how I got this

## FAQ

Q: What is diceware?

A: See http://world.std.com/~reinhold/diceware.html



Q: Is this safe?

A: See http://world.std.com/~reinhold/diceware.html



Q: Should you really be publishing the wordlist you use?

A: See http://world.std.com/~reinhold/diceware.html (Are you sensing a pattern here?)

PS: In the future, I plan on adding options to select a random wordlist from a directory for each word in the passphrase.



Q: Why "ChopWare"?

A: Diceware -> dice -> dicing -> chopping -> chopware.... Hey, it's more creative than "PassSelector" or something
