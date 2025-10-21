from typing import Tuple

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm to find modular inverse.
    Returns gcd, x, y such that ax + by = gcd(a, b).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a: int, m: int) -> int:
    """
    Modular multiplicative inverse of a modulo m.
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def affine_encrypt(text: str, key_a: int, key_b: int) -> str:
    """
    Encrypts plaintext using the Affine cipher.
    Ciphertext = (a * P + b) mod 26
    """
    result = ""
    for char in text.upper():
        if char.isalpha():
            # Convert char to a number (A=0, B=1, ...)
            p = ord(char) - ord('A')
            # Apply encryption formula
            c = (key_a * p + key_b) % 26
            # Convert number back to char
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def affine_decrypt(ciphertext: str, key_a: int, key_b: int) -> str:
    """
    Decrypts ciphertext using the Affine cipher.
    Plaintext = a^-1 * (C - b) mod 26
    """
    result = ""
    try:
        mod_inv_a = modinv(key_a, 26)
    except Exception as e:
        return f"Error: {e}. 'a' ({key_a}) must be coprime with 26."

    for char in ciphertext.upper():
        if char.isalpha():
            # Convert char to a number (A=0, B=1, ...)
            c = ord(char) - ord('A')
            # Apply decryption formula
            p = (mod_inv_a * (c - key_b)) % 26
            # Convert number back to char
            result += chr(p + ord('A'))
        else:
            result += char
    return result

if __name__ == '__main__':
    while True:
        print("\nAffine Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice in ('1', '2'):
            try:
                a = int(input("Enter key 'a' (must be coprime with 26, e.g., 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25): "))
                b = int(input("Enter key 'b' (an integer): "))
                message = input("Enter the message: ")

                if choice == '1':
                    encrypted_message = affine_encrypt(message, a, b)
                    print(f"\nEncrypted Message: {encrypted_message}")
                else: # choice == '2'
                    decrypted_message = affine_decrypt(message, a, b)
                    print(f"\nDecrypted Message: {decrypted_message}")

            except ValueError:
                print("Invalid key. Please enter integers for 'a' and 'b'.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
