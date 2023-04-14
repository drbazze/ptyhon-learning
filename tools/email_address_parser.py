#Get the input
email = input("add your email address: ").strip()

try:
    name = email[:email.index("@")]
    domain = email[email.index("@")+1:]

    print('''
    Aproach one is about finding the @ character's index in the input and slice the text based on this index
    ''')
    print(f"name: {name}")
    print(f"domain: {domain}")


    emailParts = email.split("@", 1)

    print('''
    Approach two is about splitting the email at the @ character. The result will be an arra with two items left from the @ and the right side of the @
    ''')
    print(f"name: {emailParts[0]}")
    print(f"domain: {emailParts[1]}")
except:
    print(f"It's not a valid email address")