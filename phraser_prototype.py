import msvcrt
#Dear future me: I hope you can remember how this "phrase memorization tool" was supposed to work.
#Dear past me: congrats. You made a stupid version of VI with less functionality than notepad.
def main():
	#Type anything until exit sequence is typed
	#Just prints the typed keys out
	#Exit sequence: *****
	exit_char = '*'
	exit_str_len = 5

	while True:
		c = str(msvcrt.getch())[2] #Get input, no need to hit enter. Doesn't work with special input chars (ctrl+c, for example)
		#										Process received code. Typing 'a' will cause msvcrt.getch() to output " b'a "
		#											and we only need 'a'
		if c == exit_char: 						#Detect first char of exit sequence
			exit_string = exit_char
			while True:							#Exit sequence process loop
				c = str(msvcrt.getch())[2]
				if c == exit_char:
					exit_string += c
				else:
					print(exit_char, end="")	#Turns any character into a postfix escape sequence for the exit char
					break
				if exit_string == exit_char*exit_str_len: #Exit program
					return
				if exit_string == exit_char*(exit_str_len-1): #Warn before entering last char
					print()
					print(f"Enter {exit_char} once more to exit. Enter anything else to continue.")		
		print(c, end="", flush=True)			#Print character. Ironically, this single line is the important part of this script

main()
