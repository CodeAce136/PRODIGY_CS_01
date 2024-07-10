def caesar_cipher(text, shift, mode):
    result = ""
    
    shift = shift % 26
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - shift_base - shift + 26) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))
    mode = input("Would you like to 'encrypt' or 'decrypt' the message? ").lower()
    
    if mode in ['encrypt', 'decrypt']:
        result = caesar_cipher(message, shift, mode)
        print(f"Resulting message: {result}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
