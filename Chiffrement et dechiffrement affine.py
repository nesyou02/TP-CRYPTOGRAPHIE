import numpy as np

# --- 1. Conversion lettres <-> chiffres ---
def lettre_vers_chiffre(texte):
    return [ord(c.upper()) - ord('A') for c in texte if c.isalpha()]

def chiffre_vers_lettre(chiffres):
    return ''.join(chr((c % 26) + ord('A')) for c in chiffres)

# --- 2. Chiffrement de Hill ---
def hill_chiffrement(texte, cle_matrice):
    taille_bloc = cle_matrice.shape[0]
    texte_num = lettre_vers_chiffre(texte)
    while len(texte_num) % taille_bloc != 0:
        texte_num.append(ord('X') - ord('A'))
    texte_chiffre = []
    for i in range(0, len(texte_num), taille_bloc):
        bloc = np.array(texte_num[i:i+taille_bloc])
        bloc_chiffre = np.dot(cle_matrice, bloc) % 26
        texte_chiffre.extend(bloc_chiffre)
    return chiffre_vers_lettre(texte_chiffre)

# --- 3. Déchiffrement de Hill ---
def hill_dechiffrement(texte_chiffre, cle_matrice):
    """
    Déchiffre un texte avec l’algorithme de Hill.
    Recalcule la matrice inverse modulo 26.
    Supprime les lettres de padding (X) à la fin si nécessaire.
    """
    from numpy.linalg import inv

    taille_bloc = cle_matrice.shape[0]
    texte_num = lettre_vers_chiffre(texte_chiffre)

    # Calcul de l'inverse de la matrice clé modulo 26
    det = int(round(np.linalg.det(cle_matrice))) % 26
    det_inv = pow(det, -1, 26)  # Inverse modulaire
    adj = np.round(det * np.linalg.inv(cle_matrice)).astype(int) % 26
    cle_inverse = (det_inv * adj) % 26

    texte_dechiffre = []

    # Traitement bloc par bloc
    for i in range(0, len(texte_num), taille_bloc):
        bloc = np.array(texte_num[i:i + taille_bloc])
        bloc_dechiffre = np.dot(cle_inverse, bloc) % 26
        texte_dechiffre.extend(bloc_dechiffre)

    # Conversion et suppression du padding éventuel
    return chiffre_vers_lettre(texte_dechiffre).rstrip("X")


# --- 4. Menu interactif ---
def lire_matrice(n):
    cle = []
    while True:
        try:
            for i in range(n):
                ligne = input(f"Ligne {i+1} : ").strip()
                valeurs = list(map(int, ligne.split()))
                if len(valeurs) != n:
                    raise ValueError
                cle.append(valeurs)
            return np.array(cle)
        except ValueError:
            print("Erreur : chaque ligne doit contenir exactement", n, "entiers.")
            cle.clear()

def menu():
    print("=== Chiffrement et Déchiffrement de Hill ===\n")
    
    texte = input("Entrez le texte à traiter : ").strip()
    
    print("\nEntrez les coefficients de la matrice clé ligne par ligne.")
    print("Exemple pour une matrice 2x2 :\n3 3\n2 5")
    cle_matrice = lire_matrice(2)

    print("\nQue souhaitez-vous faire ?")
    print("1. Chiffrer le texte")
    print("2. Déchiffrer le texte")
    print("3. Quitter")
    choix = input("Votre choix : ").strip()

    if choix == "1":
        resultat = hill_chiffrement(texte, cle_matrice)
        print(f"\nTexte chiffré : {resultat}")

    elif choix == "2":
        resultat = hill_dechiffrement(texte, cle_matrice)
        if resultat is not None:  # si le déchiffrement a bien réussi
            print(f"\nTexte déchiffré : {resultat}")

    elif choix == "3":
        print("Fin du programme.")

    else:
        print("Choix invalide.")

# --- Point d'entrée ---
if __name__ == "__main__":
    menu()
