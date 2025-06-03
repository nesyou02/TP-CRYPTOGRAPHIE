# Fonction de chiffrement de César
def cesar_chiffrement(message, cle):
    decalage = len(cle)  # Le décalage est basé sur la longueur de la clé
    resultat = ""  # Chaîne résultat à construire

    for char in message:
        if char.islower():  # Si c'est une lettre minuscule
            # Décale la lettre dans l'alphabet minuscule
            resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        elif char.isupper():  # Si c'est une lettre majuscule
            # Décale la lettre dans l'alphabet majuscule
            resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        else:
            # Si ce n'est pas une lettre, on ne le modifie pas (espaces, ponctuations...)
            resultat += char
    return resultat  # On retourne le message chiffré


# Fonction de déchiffrement de César (opération inverse)
def cesar_dechiffrement(message, cle):
    decalage = len(cle)  # Même principe : on utilise la longueur de la clé
    resultat = ""

    for char in message:
        if char.islower():
            # Décalage inverse pour retrouver la lettre d'origine
            resultat += chr((ord(char) - ord('a') - decalage) % 26 + ord('a'))
        elif char.isupper():
            resultat += chr((ord(char) - ord('A') - decalage) % 26 + ord('A'))
        else:
            # Caractères non alphabétiques restent inchangés
            resultat += char
    return resultat


# Fonction principale qui gère l'interaction avec l'utilisateur
def main():
    print("=== Chiffrement César ===")
    # Demande à l'utilisateur s'il veut chiffrer ou déchiffrer
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        # Cas du chiffrement
        message = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé de chiffrement (ex: ABC) : ")
        crypte = cesar_chiffrement(message, cle)  # Appel de la fonction de chiffrement
        print("\nMessage chiffré :", crypte)

    elif choix == 'D':
        # Cas du déchiffrement
        message = input("Entrez le message à déchiffrer : ")
        cle = input("Entrez la clé de chiffrement utilisée : ")
        decrypte = cesar_dechiffrement(message, cle)  # Appel de la fonction de déchiffrement
        print("\nMessage déchiffré :", decrypte)

    else:
        # Si l'utilisateur ne tape ni C ni D
        print("Choix invalide. Tapez 'C' pour chiffrer ou 'D' pour déchiffrer.")


# Lancement du programme si ce fichier est exécuté directement
if __name__ == "__main__":
    main()