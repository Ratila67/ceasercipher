import string
from typing import Any
import script_dechiff as sd

def cesar_cipher(text, key, cipher):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + (1 if cipher else -1) * key) % 1_114_112) 
		for char in text]) # on chiffre ou déchiffre le texte avec la clé
	else:
		raise(TypeError)


def hack_cesar_cipher(crypted_text, alphabet):
	if type(crypted_text) == str and type(alphabet) == str:
		for possible_key in range(0, 1_114_112):
			possible_uncryption = cesar_cipher(crypted_text, possible_key, cipher=False)
			if possible_uncryption[0] in alphabet:
				print(possible_key)
				print(possible_uncryption)
				print("_"*20)
	else:
		raise(TypeError)


def vigenere_cipher(text, password, cipher):
	list_of_crypted_chars = []
	list_of_keys = [ord(char) for char in password]
	
	for index, current_char in enumerate(text):
		
		current_key = list_of_keys[index % len(list_of_keys)]
		current_crypted_char = cesar_cipher(current_char, current_key, cipher)

		list_of_crypted_chars.append(current_crypted_char)

	crypted_text = "".join(list_of_crypted_chars)

	return crypted_text


def crypt_cesar(text,key):
	crypted_text = ""
	for char in text: # on parcourt le texte
		# On calcule le nouveau code ASCII en ajoutant la clé
		# Le modulo garantit que le résultat reste dans la plage valide (0 à 93+33 afin d'avoir les caractères ASCII valides)
		new_code = (ord(char) + key) % 93 + 33
		crypted_char = chr(new_code) # on convertit le code en caractère
		crypted_text += crypted_char # on ajoute le caractère chiffré au résultat
	return crypted_text

def decrypt_cesar(text,key):
	decrypted_text = ""
	for char in text: # on parcourt le texte crypté
		# On calcule le nouveau code ASCII en ajoutant la clé
		# Le modulo garantit que le résultat reste dans la plage valide (0 à 93+33 afin d'avoir les caractères ASCII valides)
		new_code = (ord(char) - key) % 93 + 33
		decrypted_char = chr(new_code) # on convertit le code en caractère
		decrypted_text += decrypted_char # on ajoute le caractère chiffré au résultat
	return decrypted_text

def crypt_vigenere(text, password):
	# Étape 4 : Chiffrement de Vigenère
	# On utilise crypt_cesar avec une clé différente pour chaque caractère
	crypted_text = ""
	for index, char in enumerate(text):
		#print(f"index {index} et char {char}, password {password}") #dans index j'ai l'index du caractère dans le texte, dans char j'ai le caractère lui même, dans password j'ai la clé de chiffrement
		key_index = index % len(password) # on récupère l'index du caractère de la clé à cette position
		#print(f"key index {key_index}")
		key_char = password[key_index] # on récupère le caractère de la clé à cette position
		#print(f"key char {key_char}")
		key_value = ord(key_char) # on convertit le caractère de la clé en nombre (son code ASCII) pour pouvoir l'utiliser comme clé de chiffrement
		#print(f"key value {key_value}")
		crypted_char = crypt_cesar(char, key_value)
		crypted_text += crypted_char
	return crypted_text

def decrypt_vigenere(text, password):
	# Étape 5 : Déchiffrement de Vigenère
	# On utilise decrypt_cesar avec les décalages inverses de la clé
	decrypted_text = ""
	for index, char in enumerate(text):
		key_index = index % len(password)
		key_char = password[key_index]
		key_value = ord(key_char)
		decrypted_char = decrypt_cesar(char, key_value)
		decrypted_text += decrypted_char
	
	return decrypted_text


if __name__ == "__main__":
	input_message = input("Entrez un message à chiffrer : ")
	input_key = int(input("Entrez un décalage de César (chiffre uniquement): "))

	input_message_crypt = input("Entrez un message à déchiffrer : ")
	input_key_decrypt = int(input("Entrez le décalage de César pour le déchiffrement: "))
	
	input_password = input("Entrez un mot de passe de chiffrement : ")

	crypted_text = crypt_cesar(input_message, input_key) # exo 1
	print("Exo 1: Voici votre message chiffré : " + crypted_text)

	initial_message = decrypt_cesar(input_message_crypt, input_key_decrypt) # exo 2
	print("Exo 2: Voici votre message déchiffré : " + initial_message + "\n" + "Le message est correct ? " + str(initial_message == input_message_crypt))

	sd.cesar_cipher_multiple(input_message) # exo3
	print("Exo 3: " + "_"*20)

	crypted_message = crypt_vigenere(input_message, input_password) # exo 4
	print("Exo 4: Voici votre message chiffré : " + crypted_message)
	initial_message = decrypt_vigenere(crypted_message, input_password) # exo 5
	print("Exo 5: Voici votre message déchiffré : " + initial_message + "\n" + "Le message est correct ? " + str(initial_message == input_message))
	print("Exo 5: Le message est correct ? " + str(initial_message == input_message))