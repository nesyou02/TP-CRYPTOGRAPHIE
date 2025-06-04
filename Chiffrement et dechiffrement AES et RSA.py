import os, base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding

# === Génération des clés RSA (asymétriques) ===
def generer_cles_rsa():
    """
    Crée une paire de clés RSA : privée et publique
    """
    cle_privee = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    cle_publique = cle_privee.public_key()
    return cle_privee, cle_publique

# === Chiffrement AES (symétrique) ===
def chiffrer_aes(message, cle_aes):
    """
    Chiffre un message texte avec AES en mode CBC.
    Retourne le IV et le message chiffré.
    """
    iv = os.urandom(16)  # vecteur d'initialisation aléatoire
    padder = sym_padding.PKCS7(128).padder()
    message_pad = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(cle_aes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    message_chiffre = encryptor.update(message_pad) + encryptor.finalize()
    return iv, message_chiffre

# === Déchiffrement AES ===
def dechiffrer_aes(iv, message_chiffre, cle_aes):
    """
    Déchiffre un message AES avec IV et clé fournie.
    """
    cipher = Cipher(algorithms.AES(cle_aes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    message_pad = decryptor.update(message_chiffre) + decryptor.finalize()

    unpadder = sym_padding.PKCS7(128).unpadder()
    message = unpadder.update(message_pad) + unpadder.finalize()
    return message.decode()

# === Chiffrement de la clé AES avec RSA ===
def chiffrer_cle_aes(cle_aes, cle_publique):
    """
    Utilise la clé publique RSA pour chiffrer la clé AES.
    """
    return cle_publique.encrypt(
        cle_aes,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# === Déchiffrement de la clé AES ===
def dechiffrer_cle_aes(cle_aes_chiffree, cle_privee):
    """
    Utilise la clé privée RSA pour déchiffrer la clé AES.
    """
    return cle_privee.decrypt(
        cle_aes_chiffree,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# === Menu interactif ===
def menu_crypto():
    print("=== Menu Chiffrement AES & RSA ===")

    # Génération d’une paire de clés à chaque exécution
    cle_privee, cle_publique = generer_cles_rsa()

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            # --- Saisie du message à chiffrer ---
            message = input("Entrez le message à chiffrer : ")
            cle_aes = os.urandom(32)  # Clé AES 256 bits

            # --- Chiffrement symétrique puis asymétrique de la clé ---
            iv, message_chiffre = chiffrer_aes(message, cle_aes)
            cle_aes_chiffree = chiffrer_cle_aes(cle_aes, cle_publique)

            print("\n=== Résultat du chiffrement ===")
            print("Message chiffré (base64) :", base64.b64encode(message_chiffre).decode())
            print("IV (base64) :", base64.b64encode(iv).decode())
            print("Clé AES chiffrée (base64) :", base64.b64encode(cle_aes_chiffree).decode())

        elif choix == "2":
            # --- Entrée des composants nécessaires au déchiffrement ---
            msg64 = input("Entrez le message chiffré (base64) : ")
            iv64 = input("Entrez l'IV (base64) : ")
            cle64 = input("Entrez la clé AES chiffrée (base64) : ")

            try:
                # --- Décodage base64 + déchiffrement ---
                message_chiffre = base64.b64decode(msg64)
                iv = base64.b64decode(iv64)
                cle_aes_chiffree = base64.b64decode(cle64)

                cle_aes = dechiffrer_cle_aes(cle_aes_chiffree, cle_privee)
                message = dechiffrer_aes(iv, message_chiffre, cle_aes)

                print("\nMessage déchiffré :", message)

            except Exception as e:
                print("Erreur de déchiffrement :", e)

        elif choix == "3":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Réessayez.")

# === Point d’entrée du programme ===
if __name__ == "__main__":
    menu_crypto()
