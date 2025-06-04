# === Programme complet pour le chiffrement et le déchiffrement affine ===

# Fonction de chiffrement affine
def chiffrement_affine(texte, a, b):
    """
    Chiffre un texte clair selon la formule affine :
    y = (a * x + b) mod 26
    Où :
      - x est la position de la lettre dans l'alphabet (A=0, ..., Z=25)
      - a et b sont des entiers choisis comme clés
    """
    texte = texte.upper()  # Convertir le texte en majuscules
    texte_chiffre = ""

    for char in texte:
        if char.isalpha():
            x = ord(char) - ord('A')               # Convertir lettre → position
            y = (a * x + b) % 26                    # Appliquer fonction affine
            texte_chiffre += chr(y + ord('A'))     # Convertir position → lettre
        else:
            texte_chiffre += char  # Garder les caractères non alphabétiques tels quels

    return texte_chiffre


# Fonction de déchiffrement affine
def dechiffrement_affine(texte_chiffre, a, b):
    """
    Déchiffre un texte chiffré avec l’algorithme affine :
    x = a⁻¹ * (y - b) mod 26
    L’inverse modulaire de a doit exister modulo 26 (a premier avec 26).
    """
    texte_chiffre = texte_chiffre.upper()
    texte_dechiffre = ""

    try:
        a_inv = pow(a, -1, 26)  # Inverse modulaire de a modulo 26
    except ValueError:
        print("Erreur : a n’a pas d’inverse modulo 26. Choisissez un 'a' premier avec 26.")
        return None

    for char in texte_chiffre:
        if char.isalpha():
            y = ord(char) - ord('A')                   # Lettre → position
            x = (a_inv * (y - b)) % 26                  # Formule inverse
            texte_dechiffre += chr(x + ord('A'))       # Position → lettre
        else:
            texte_dechiffre += char  # Garder ponctuation, espaces, etc.

    return texte_dechiffre


# Menu interactif pour l'utilisateur
def menu_affine():
    print("=== Chiffrement et Déchiffrement Affine ===\n")

    texte = input("Entrez le texte à traiter : ").strip()

    # Récupérer les clés
    try:
        a = int(input("Entrez la clé 'a' (doit être premier avec 26) : "))
        b = int(input("Entrez la clé 'b' (entier quelconque) : "))
    except ValueError:
        print("Erreur : les clés doivent être des entiers.")
        return

    # Choix de l'action
    print("\nQue souhaitez-vous faire ?")
    print("1. Chiffrer le texte")
    print("2. Déchiffrer le texte")
    print("3. Quitter")

    choix = input("Votre choix : ").strip()

    if choix == "1":
        resultat = chiffrement_affine(texte, a, b)
        print(f"\nTexte chiffré : {resultat}")
    elif choix == "2":
        resultat = dechiffrement_affine(texte, a, b)
        if resultat is not None:
            print(f"\nTexte déchiffré : {resultat}")
    elif choix == "3":
        print("Fin du programme.")
    else:
        print("Choix invalide.")


# Point d'entrée du programme
if __name__ == "__main__":
    menu_affine()