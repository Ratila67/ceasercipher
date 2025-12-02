import string
import cryptography as cr

def cesar_cipher_multiple(text):
    for d in range(len(string.printable)):
        result = cr.crypt_cesar(text, d)   # on déchiffre le texte avec la clé d
        print(result + "\n" + "Decalage: " + str(d))
        print("_"*20)

if __name__ == "__main__":
    text = "lapin"
    cesar_cipher_multiple(text)
    print("_"*20)