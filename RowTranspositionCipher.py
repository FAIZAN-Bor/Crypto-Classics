import math
from typing import List

def row_transposition_encrypt(plain_text: str, key: str) -> str:
    """
    Encrypts a message using the Row Transposition cipher.
    """
    # Remove spaces and convert to uppercase for simplicity
    plain_text = plain_text.replace(" ", "").upper()
    key_map = sorted([(int(k), i) for i, k in enumerate(key)])
    num_cols = len(key)
    num_rows = math.ceil(len(plain_text) / num_cols)

    # Pad the message if its length is not a multiple of the key length
    padded_text = plain_text.ljust(num_rows * num_cols, 'X')

    # Create the matrix
    matrix = [list(padded_text[i:i + num_cols]) for i in range(0, len(padded_text), num_cols)]

    # Read the ciphertext column by column based on the key order
    cipher_text = ""
    for _, col_index in key_map:
        for row in range(num_rows):
            cipher_text += matrix[row][col_index]

    return cipher_text

def row_transposition_decrypt(cipher_text: str, key: str) -> str:
    """
    Decrypts a message encrypted with the Row Transposition cipher.
    """
    key_map = sorted([(int(k), i) for i, k in enumerate(key)])
    num_cols = len(key)
    num_rows = math.ceil(len(cipher_text) / num_cols)
    
    # Create an empty matrix to fill with the ciphertext
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Calculate how many full columns and how many shorter columns there are
    # This is needed if the original message wasn't perfectly divisible
    str_idx = 0
    full_cols = len(cipher_text) % num_cols
    
    # Fill the matrix column by column using the key order
    cipher_idx = 0
    for _, col_index in key_map:
        # Determine the length of the current column
        col_len = num_rows if col_index < full_cols or full_cols == 0 else num_rows - 1
        for row in range(col_len):
            matrix[row][col_index] = cipher_text[cipher_idx]
            cipher_idx += 1
            
    # Read the plaintext row by row
    plain_text = "".join(["".join(row) for row in matrix])
    return plain_text

if __name__ == '__main__':
    while True:
        print("\nRow Transposition Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice in ('1', '2'):
            try:
                message = input("Enter the message: ")
                key_str = input("Enter the numerical key (e.g., 3142): ")
                # Basic validation for the key
                if not key_str.isdigit() or len(set(key_str)) != len(key_str):
                    print("Invalid key. It must be a sequence of unique digits.")
                    continue

                if choice == '1':
                    encrypted = row_transposition_encrypt(message, key_str)
                    print(f"\nEncrypted Message: {encrypted}")
                else: # choice == '2'
                    decrypted = row_transposition_decrypt(message, key_str)
                    print(f"\nDecrypted Message: {decrypted}")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
