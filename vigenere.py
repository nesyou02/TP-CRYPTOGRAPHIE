# Fonction de chiffrement de Vigenère
def vigenere_chiffrement(message, cle):
    resultat = ""
    cle = cle.upper()      # On met la clé en majuscules
    message = message.upper()  # On met aussi le message en majuscules
    i = 0  # Index pour parcourir les lettres de la clé

    for char in message:
        if char.isalpha():  # Si le caractère est une lettre
            # Calcule le décalage à appliquer (ex: 'B' -> 1, 'C' -> 2, ...)
            decalage = ord(cle[i % len(cle)]) - ord('A')
            # Décale la lettre dans l'alphabet en tenant compte du décalage
            nouveau = chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
            resultat += nouveau
            i += 1  # On passe à la lettre suivante de la clé
        else:
            # Caractères non alphabétiques restent inchangés
            resultat += char
    return resultat


# Fonction de déchiffrement de Vigenère
def vigenere_dechiffrement(message, cle):
    resultat = ""
    cle = cle.upper()
    message = message.upper()
    i = 0

    for char in message:
        if char.isalpha():
            # Même logique, mais on soustrait le décalage
            decalage = ord(cle[i % len(cle)]) - ord('A')
            original = chr((ord(char) - ord('A') - decalage) % 26 + ord('A'))
            resultat += original
            i += 1
        else:
            resultat += char
    return resultat


# Fonction principale avec interaction utilisateur
def main():
    print("=== Chiffrement de Vigenère ===")
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        message = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé : ")
        crypte = vigenere_chiffrement(message, cle)
        print("\nMessage chiffré :", crypte)

    elif choix == 'D':
        message = input("Entrez le message à déchiffrer : ")
        cle = input("Entrez la clé utilisée : ")
        decrypte = vigenere_dechiffrement(message, cle)
        print("\nMessage déchiffré :", decrypte)

    else:
        print("Choix invalide. Tapez 'C' pour chiffrer ou 'D' pour déchiffrer.")


# Lancement automatique
if __name__ == "__main__":
    main()

