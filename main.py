#############################################
#------------FUNCTIONS FOR FILES------------#

#this is a function that opens files
def open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word.lower())
		output.append(line_words)
	return (output)

#this is a function that writes files
def write_file(filename, data):
	new_file = open(filename, "w")
	for sentence in data:
		for word in sentence:
			new_file.write(word + " ")
		new_file.write("\n")
	new_file.close()

##############################################
#------------FUNCTIONS FOR CIPHER------------#

def encrypt_letter(letter, key):
  #key = [multiplier, shift]
  #encryption formula    
  char_number = ord(letter) - ord("a")
  enc_char_number = (key[0]*char_number + key[1])%26 
  return(chr(enc_char_number + ord("a")))

def decrypt_letter(letter, key):
  #decryption formula
  inverse = find_inverse(key[0])
  char_number = ord(letter) - ord("a")
  dec_char_number = ((char_number - key[1])*inverse)%26 
  return(chr(dec_char_number + ord("a")))

def encrypt_word(word, key):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  cipher_word = ""
  for letter in word:
    if letter in letters:
      cipher_word += encrypt_letter(letter, key)
    else:
      cipher_word += letter
  return cipher_word

def decrypt_word(word, key):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  plain_word = ""
  for letter in word:
    if letter in letters:
      plain_word += decrypt_letter(letter, key)
    else:
      plain_word += letter
  return plain_word

def encrypt_message(message, key):
  cipher_message =[]
  for line in message:
    cipher_line = []
    for word in line:
      cipher_line.append(encrypt_word(word, key))
    cipher_message.append(cipher_line)
  return cipher_message

def decrypt_message(message, key):
  plain_message =[]
  for line in message:
    plain_line = []
    for word in line:
      plain_line.append(decrypt_word(word, key))
    plain_message.append(plain_line)
  return plain_message

#this function returns the inverse of a modulo 26
def find_inverse(num):
  for i in range(1000000):
    if num*i %26 == 1:
      return i

###### TESTING CODE HERE ######
#multplier can be most odd numbers(not divisble by 13) :)
multiplier = 31
#shift can be ANY nunmber
shift = 20 
key = [multiplier, shift] #list of two items
#PKE uses 256 bit keys (thats 2^256)

#prints the key of the plain text to the cipher one
for plain in range(26):
  cipher = (key[0]*plain + key[1]) % 26
  print(chr(plain + ord("a")), "=", chr((cipher + ord("a"))))

write_file('enc_message', [['jmy']]) #encoded message of 'dog'
encrypted_message = open_file('enc_message')
decrypted_message = decrypt_message(encrypted_message, key)
write_file('dec_message', decrypted_message)
####################################

plainQuote = open_file('plain_text') 
#encrypt it
encryptQuote = encrypt_message(plainQuote, key)
#write it to cipher_text
write_file('cipher_text', encryptQuote)
#decryption
decryptQuote = decrypt_message(encryptQuote, key)
write_file('decrypted_text', decryptQuote)

#######################################
#---------WORK GROUP 2 CIPHER----------#
"""
multiplier = 63
shift = 25
key = [multiplier, shift]

sample = open_file('wg2')
print(decrypt_message(sample, key))

#[['when', 'someone', 'shows', 'you', 'who', 'they', 'are,'], ['believe', 'them', 'the', 'first', 'time.'], ['-maya', 'angelou']]

"""