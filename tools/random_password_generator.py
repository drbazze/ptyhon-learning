"""
Project:
A random passoword genator that allows the user to add the lenght and the complexity.

Requirements:
- The length must be added my the user and it must be minimum 4
- There must be 3 complexities:
    - Basic: numbers + letters
    - Medium: numbers + letters (min 2 lowercase, min 2 uppercase)
    - Strong: numbers = letters = special chars (min 2 lowercase, min 2 uppercase, min 1 special character)
- The user must select from the predefined complexity list
"""
import random
import string

"""
The main function
@param integer length = length of the password (limit is 128)
@param integer complexity = index for the complexity charsets
"""
def generatePassword (length, complexity):  
    #Defaults
    defLength = 12
    defComplexityOption = 2 #Numbers and Letters

    #Check if the length input is in the range
    if (length < 4 or length > 128):
        length = defLength
        print(f"Default lenght is added {length}")

    #Check if the complexity input is in the range
    if (complexity < 1 or complexity > 3):
        complexity = defComplexityOption
        print(f"Default complexity is added {complexity}")

    #Complexities list. The input option numbers must be the same.
    complexities = [
        string.digits, #Numbers only
        string.ascii_letters + string.digits, #Numbers and Letters
        string.ascii_letters + string.digits + string.punctuation #Numbers and Letters and Special Characters
    ]

    #Get the characters accoring to the inputs. The complexity must be shifted due to the index
    charset = complexities[complexity-1]
    # Generate a password by randomly selecting characters from the charset
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

if __name__ == "__main__":
    print('''Welcome to the password generator!
    ''')

    # Getting password length
    length = int(input("Enter password length between 4-128: "))

    print('''Choose the complexity :
            1. Numbers
            2. Numbers and Letters
            3. Numbers and Letters and Special Characters''')

    complexity = int(input("Pick a number "))

    password = generatePassword(length, complexity)

    print(f"password: {password}")