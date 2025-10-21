def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypts a given plaintext using the Caesar cipher.

    Args:
        text (str): The plaintext message to encrypt.
        shift (int): The number of positions to shift letters.

    Returns:
        str: The encrypted ciphertext.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('a') if char.islower() else ord('A')
            # Calculate the shifted position
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Non-alphabetic characters are not changed
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts a given ciphertext using the Caesar cipher.

    Args:
        text (str): The ciphertext message to decrypt.
        shift (int): The number of positions the letters were shifted by.

    Returns:
        str: The decrypted plaintext.
    """
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(text, -shift)

if __name__ == '__main__':
    while True:
        print("\nCaesar Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice == '1':
            try:
                message = input("Enter the message to encrypt: ")
                shift_key = int(input("Enter the shift value (an integer): "))
                encrypted_message = caesar_encrypt(message, shift_key)
                print(f"\nEncrypted Message: {encrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '2':
            try:
                message = input("Enter the message to decrypt: ")
                shift_key = int(input("Enter the shift value (an integer): "))
                decrypted_message = caesar_decrypt(message, shift_key)
                print(f"\nDecrypted Message: {decrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
