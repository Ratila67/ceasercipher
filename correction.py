def cesar_cipher_correction(text, key, cipher=True):

    key = key if cipher else -key # si cipher est True, on utilise la clé, sinon on utilise la clé négative

    crypted_text = ""
    for char in text: # on parcourt le texte
        crypted_char = chr((ord(char) + key) % 1_114_112) # ord permet de prendre la position ascii et % 1_114_112 permet de rester dans la plage valide (0 à 1_114_112)
        crypted_text += crypted_char # on ajoute le caractère chiffré au résultat

    return crypted_text


initial_message = "le chocolat est bon"

crypted_message = cesar_cipher_correction(initial_message, 12)
print(crypted_message) # on chiffre le message avec la clé 12

print(cesar_cipher_correction(crypted_message, 12, False)) # on déchiffre le message avec la clé négative