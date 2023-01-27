try: 
	import pyperclip
except ImportError:
	pass

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

while True:
	print('Enter a message to encrypt/decrypt (or QUIT):')
	message = input('> ')

	if message.upper() == 'QUIT':
		break

	print(message)
	translated = ''
	for character in message:
		if character.isupper():
			transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
			translated += UPPER_LETTERS[transCharIndex]
		elif character.islower():
			transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
			translated += LOWER_LETTERS[transCharIndex]
		else:
			translated += character

	print('The translated essage is:')
	print(translated)
	print()

	try: 
		pyperclip.copy(translated)
		print('(Copied to clipboard.)')
	except:
		pass