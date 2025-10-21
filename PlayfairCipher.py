from typing import List, Tuple

def generate_key_matrix(key: str) -> List[List[str]]:
    """
    Generates the 5x5 key matrix for the Playfair cipher.
    """
    key = key.upper().replace(" ", "").replace("J", "I")
    matrix = []
    # Add unique characters from the key to the matrix
    for char in key:
        if char not in matrix:
            matrix.append(char)

    # Add the remaining alphabet characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    # Reshape the list into a 5x5 matrix
    key_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix

def find_position(key_matrix: List[List[str]], char: str) -> Tuple[int, int]:
    """
    Finds the row and column of a character in the key matrix.
    """
    for r, row in enumerate(key_matrix):
        for c, value in enumerate(row):
            if value == char:
                return r, c
    return -1, -1 # Should not happen with valid input

def prepare_plaintext(plaintext: str) -> List[str]:
    """
    Prepares the plaintext for Playfair encryption.
    - Converts to uppercase
    - Replaces 'J' with 'I'
    - Splits into digraphs, handling double letters with 'X'
    - Pads with 'X' if the length is odd
    """
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    prepared_text = ""
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        prepared_text += char1
        if i + 1 < len(plaintext):
            char2 = plaintext[i+1]
            if char1 == char2:
                prepared_text += 'X'
                i += 1
            else:
                prepared_text += char2
                i += 2
        else:
            prepared_text += 'X'
            i += 1
    return [prepared_text[i:i + 2] for i in range(0, len(prepared_text), 2)]

def playfair_crypt(text_pairs: List[str], key_matrix: List[List[str]], mode: int) -> str:
    """
    Performs Playfair encryption or decryption.
    mode = 1 for encrypt, -1 for decrypt.
    """
    result = ""
    for pair in text_pairs:
        char1, char2 = pair[0], pair[1]
        r1, c1 = find_position(key_matrix, char1)
        r2, c2 = find_position(key_matrix, char2)

        if r1 == r2:  # Same row
            result += key_matrix[r1][(c1 + mode) % 5]
            result += key_matrix[r2][(c2 + mode) % 5]
        elif c1 == c2:  # Same column
            result += key_matrix[(r1 + mode) % 5][c1]
            result += key_matrix[(r2 + mode) % 5][c2]
        else:  # Rectangle
            result += key_matrix[r1][c2]
            result += key_matrix[r2][c1]
    return result

def main() -> None:
    while True:
        print("\nPlayfair Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice in ('1', '2'):
            keyword = input("Enter the keyword: ")
            key_matrix = generate_key_matrix(keyword)
            print("\nGenerated 5x5 Key Matrix:")
            for row in key_matrix:
                print(" ".join(row))

            message = input("Enter the message: ")

            if choice == '1':
                plaintext_pairs = prepare_plaintext(message)
                encrypted = playfair_crypt(plaintext_pairs, key_matrix, 1)
                print(f"\nPrepared Plaintext (Digraphs): {' '.join(p for p in plaintext_pairs)}")
                print(f"Encrypted Message: {encrypted}")
            else: # choice == '2'
                # Normalize ciphertext: uppercase, remove spaces, replace J with I
                norm = message.upper().replace(" ", "").replace("J", "I")
                # If odd length, pad with X to form complete digraphs
                if len(norm) % 2 == 1:
                    norm += 'X'
                ciphertext_pairs = [norm[i:i + 2] for i in range(0, len(norm), 2)]
                decrypted = playfair_crypt(ciphertext_pairs, key_matrix, -1)
                print(f"\nDecrypted Message: {decrypted}")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
