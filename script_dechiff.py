import string

def dechiffre_multiple_cesare(text):
    alphabet = string.ascii_letters # alphabet en minuscule et majuscule
    for d in range(len(alphabet)):
        resultat = []
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                nouvelle_position = (position - d) % len(alphabet)
                nouvelle_lettre = alphabet[nouvelle_position]
                resultat.append(nouvelle_lettre)
            else:    
                resultat.append(char)
        print("".join(resultat) + " " + "///Decalage: " + str(d))

if __name__ == "__main__":
    text = "lapin"
    dechiffre_multiple_cesare(text)
    print("_"*20)