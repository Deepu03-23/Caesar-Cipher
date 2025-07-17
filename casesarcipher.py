def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    if mode == 'decrypt':
        shift = -shift  
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
def main():
    print("Caesar Cipher Program")
    mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()   
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
        if not (0 <= shift <= 25):
            raise ValueError
    except ValueError:
        print("Invalid shift value. Please enter an integer between 0 and 25.")
        return
    result = caesar_cipher(message, shift, mode)
    print(f"\nYour {mode}ed message is:\n{result}")
if __name__ == "__main__":
    main()
