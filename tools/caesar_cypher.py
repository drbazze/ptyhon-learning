def crypt_text(crypt_mode, text, shift_amount):
    """Encrypt/Decrypt a text"""
    #The alphabet is added two times in order to avoid the out of index error
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if crypt_mode < 1 or crypt_mode > 2:
        return "Only encode or decode commands are accepted"

    #That makes sure the shift will be in the range of 26 (aplhabet number) all the time
    shift_amount = shift_amount % 26

    #Change the direction
    if crypt_mode == "decode":
        shift_amount *= -1

    result_text = ""

    for char in text:
        if char in alphabet:
            shifted_index = alphabet.index(char) + shift_amount
            result_text += alphabet[shifted_index]
        else:
            result_text += char

    return result_text


print('''Choose the mode :
1. Encrypt
2. Decrypt''')
mode = int(input("Pick a number "))
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

result = crypt_text(mode, text, shift)

print(result)