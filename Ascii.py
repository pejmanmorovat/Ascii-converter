def text_to_decimal(text):
    return ' '.join(str(ord(char)) for char in text)

def text_to_hex(text):
    return ' '.join(hex(ord(char))[2:] for char in text)

def decimal_to_text(decimal_str):
    try:
        decimals = list(map(int, decimal_str.split()))
        return ''.join(chr(code) for code in decimals if 0 <= code <= 127)
    except ValueError:
        return "Invalid decimal ASCII code!"

def hex_to_text(hex_str):
    try:
        hexes = hex_str.split()
        return ''.join(chr(int(h, 16)) for h in hexes if 0 <= int(h, 16) <= 127)
    except ValueError:
        return "Invalid hexadecimal ASCII code!"

def main():
    print("ASCII Converter for Termux")
    print("1. Convert text to ASCII code (decimal)")
    print("2. Convert text to ASCII code (hexadecimal)")
    print("3. Convert ASCII code (decimal) to text")
    print("4. Convert ASCII code (hexadecimal) to text")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            text = input("Enter text to convert to decimal ASCII: ")
            print("Decimal ASCII codes:", text_to_decimal(text))
        elif choice == '2':
            text = input("Enter text to convert to hex ASCII: ")
            print("Hexadecimal ASCII codes:", text_to_hex(text))
        elif choice == '3':
            dec_str = input("Enter decimal ASCII codes (space-separated): ")
            print("Text:", decimal_to_text(dec_str))
        elif choice == '4':
            hex_str = input("Enter hexadecimal ASCII codes (space-separated): ")
            print("Text:", hex_to_text(hex_str))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
