from typing import List

def rail_fence_encrypt(plain_text: str, rails: int) -> str:
    """
    Encrypts a message using the Rail Fence cipher.
    """
    # Handle trivial cases gracefully
    if rails <= 1 or len(plain_text) <= 1:
        return plain_text
    # Create a fence (a list of lists)
    fence: List[List[str]] = [[] for _ in range(rails)]
    rail = 0
    direction = 1 # 1 for down, -1 for up

    # Fill the fence in a zig-zag pattern
    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        # Change direction at the top and bottom rails
        if rail == rails - 1 or rail == 0:
            direction *= -1

    # Read the fence row by row to get the ciphertext
    cipher_text = "".join(["".join(row) for row in fence])
    return cipher_text

def rail_fence_decrypt(cipher_text: str, rails: int) -> str:
    """
    Decrypts a message encrypted with the Rail Fence cipher.
    """
    if rails <= 1:
        return cipher_text

    # 1. Create a fence with placeholder markers to map the zig-zag pattern
    fence: List[List[str]] = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    # 2. Fill the fence with the ciphertext characters row by row
    cipher_index = 0
    for r in range(rails):
        for c in range(len(cipher_text)):
            if fence[r][c] == '*':
                fence[r][c] = cipher_text[cipher_index]
                cipher_index += 1

    # 3. Read the fence in the zig-zag pattern to get the plaintext
    plain_text = ""
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        plain_text += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    return plain_text

def main() -> None:
    while True:
        print("\nRail Fence Cipher Program")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1/2/3): ")

        if choice in ('1', '2'):
            try:
                message = input("Enter the message: ")
                depth = int(input("Enter the number of rails (depth): "))
                if depth < 2:
                    print("Number of rails must be 2 or more.")
                    continue

                if choice == '1':
                    encrypted = rail_fence_encrypt(message, depth)
                    print(f"\nEncrypted Message: {encrypted}")
                else: # choice == '2'
                    decrypted = rail_fence_decrypt(message, depth)
                    print(f"\nDecrypted Message: {decrypted}")

            except ValueError:
                print("Invalid number of rails. Please enter an integer.")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
