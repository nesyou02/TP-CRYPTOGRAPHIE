
import math
from collections import Counter

# --- 1. Entropie ---
def calcul_entropie(texte):
    """
    Calcule l'entropie d'un texte.
    L'entropie mesure la quantité moyenne d'information par caractère.
    """
    freqs = Counter(texte)
    total = len(texte)
    entropie = 0
    for freq in freqs.values():
        p = freq / total
        entropie -= p * math.log2(p)
    return round(entropie, 4)

# --- 2. Redondance ---
def calcul_redondance(entropie, alphabet_size=26):
    """
    Calcule la redondance du texte.
    Redondance = 1 - (entropie réelle / entropie maximale possible)
    """
    max_entropy = math.log2(alphabet_size)
    redondance = 1 - (entropie / max_entropy)
    return round(redondance, 4)

# --- 3. Indice de coïncidence ---
def indice_coincidence(texte):
    """
    Calcule l'indice de coïncidence.
    Permet de déterminer si un texte est aléatoire ou non.
    """
    freqs = Counter(texte)
    total = len(texte)
    somme = sum(f * (f - 1) for f in freqs.values())
    ic = somme / (total * (total - 1)) if total > 1 else 0
    return round(ic, 4)

# --- 4. Analyse complète ---
def analyser_texte(texte):
    """
    Effectue l'analyse complète : entropie, redondance, indice de coïncidence.
    Nettoie le texte en supprimant les espaces et en mettant en minuscules.
    """
    texte = texte.replace(" ", "").lower()
    entropie = calcul_entropie(texte)
    redondance = calcul_redondance(entropie)
    ic = indice_coincidence(texte)

    print("\n--- Analyse du texte ---")
    print(f"Entropie : {entropie}")
    print(f"Redondance : {redondance}")
    print(f"Indice de coïncidence : {ic}")

# --- 5. Menu interactif ---
def menu():
    while True:
        print("\nMenu :")
        print("1 - Saisir un texte pour analyse")
        print("2 - Quitter")
        choix = input("Choix : ")

        if choix == "1":
            texte = input("Entrez le texte à analyser : ")
            analyser_texte(texte)
        elif choix == "2":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")

# --- 6. Point d'entrée principal ---
if __name__ == "__main__":
    menu()
