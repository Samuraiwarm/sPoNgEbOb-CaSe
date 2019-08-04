START_UPPERCASE = False

user_input = input('> ').lower()

status = START_UPPERCASE

user_output = ''

for character in user_input:
	if character.isalpha() and status:
		user_output += character.upper()
		status = not status
	elif character.isalpha():
		user_output += character
		status = not status
	else:
		user_output += character

print(user_output)