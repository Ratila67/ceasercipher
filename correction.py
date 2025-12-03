import string

def cesar_cipher_correction(text, key, cipher=True):

    key = key if cipher else -key # si cipher est True, on utilise la clé, sinon on utilise la clé négative

    list_of_crypted_chars = []
    for char in text: # on parcourt le texte
        crypted_char = chr((ord(char) + key) % 1_114_112) # ord permet de prendre la position ascii et % 1_114_112 permet de rester dans la plage valide (0 à 1_114_112)
        list_of_crypted_chars.append(crypted_char) # on ajoute le caractère chiffré au résultat

    return "".join(list_of_crypted_chars)

def brute_force_cesar_cipher(crypted_text):
    for potential_key in range(0, 1_114_112):
        potentiel_intial_text = cesar_cipher_correction(crypted_text, potential_key, False)

        for char in potentiel_intial_text:
            if char in string.printable:
                print(potentiel_intial_text)
                print(potential_key)
                print("_"*20)
                break

def vigenere_cipher_correction(text, password, cipher=True):
    list_of_keys = [ord(char) for char in password]
    list_of_crypted_chars = []
    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_char = cesar_cipher_correction(char, current_key, cipher)
        list_of_crypted_chars.append(crypted_char)
    return "".join(list_of_crypted_chars)

initial_message = "Bonjour tout le monde"
password = "Azerty12345"

crypted_text = vigenere_cipher_correction(initial_message, password)
print(crypted_text)

print(vigenere_cipher_correction(crypted_text, password, False))

#initial_message = "le chocolat est bon"
#password = "Azerty12345!"
#crypted_message = cesar_cipher_correction(initial_message, 12)
#print(crypted_message) # on chiffre le message avec la clé 12

#print(cesar_cipher_correction(crypted_message, 12, False)) # on déchiffre le message avec la clé négative

#brute_force_cesar_cipher(crypted_message)
