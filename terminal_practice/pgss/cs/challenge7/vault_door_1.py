print("Sometimes, you'll have to do some decoding...")



alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift_one(word):

	shifted_word = ""
	for c in word:
		index = alphabet.find(c)
		shifted_index = (index + 1) % 26
		shifted_word = shifted_word + alphabet[shifted_index]
	return shifted_word





password = input("Password please!\n")

shifted_password = shift_one(password)

if shifted_password == "pgss":
	print("The flag is: picoCTF{" + password + "}")
else:
	print("Wrong password! Try again!")
