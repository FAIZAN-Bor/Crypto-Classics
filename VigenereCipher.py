from typing import List

def generate_key(message: str, key: str) -> str:
    """
    Generates a key of the same length as the message by repeating the keyword.
    Keeps the result as a string to preserve typing consistency.
    """
    if len(key) >= len(message):
        return key[:len(message)]
    repeats, remainder = divmod(len(message), len(key))
    return (key * repeats) + key[:remainder]

def vigenere_encrypt(message: str, key: str) -> str:
    """
    Encrypts a message using the Vigenère cipher.
    """
    encrypted_text = ""
    full_key = generate_key(message, key)
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            # Determine the case for correct shift calculation
            start = ord('a') if char.islower() else ord('A')
            key_start = ord('a') if full_key[i].islower() else ord('A')

            # Calculate the shift
            shift = ord(full_key[i]) - key_start
            # Encrypt the character
            encrypted_char_ord = (ord(char) - start + shift) % 26
            encrypted_text += chr(encrypted_char_ord + start)
        else:
            # Keep non-alphabetic characters as they are
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts a ciphertext using the Vigenère cipher.
    """
    decrypted_text = ""
    full_key = generate_key(ciphertext, key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Determine the case for correct shift calculation
            start = ord('a') if char.islower() else ord('A')
            key_start = ord('a') if full_key[i].islower() else ord('A')

            # Calculate the shift
            shift = ord(full_key[i]) - key_start
            # Decrypt the character
            decrypted_char_ord = (ord(char) - start - shift + 26) % 26
            decrypted_text += chr(decrypted_char_ord + start)
        else:
            # Keep non-alphabetic characters as they are
            decrypted_text += char
    return decrypted_text

if __name__ == '__main__':
    while True:
        print("\nVigenère Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice in ('1', '2'):
            message = input("Enter the message: ")
            keyword = input("Enter the keyword: ")
            if not keyword.isalpha():
                print("Keyword must only contain alphabetic characters.")
                continue

            if choice == '1':
                encrypted = vigenere_encrypt(message, keyword)
                print(f"\nEncrypted Message: {encrypted}")
            else: # choice == '2'
                decrypted = vigenere_decrypt(message, keyword)
                print(f"\nDecrypted Message: {decrypted}")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
