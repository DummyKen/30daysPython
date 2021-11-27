#Question
# Create a "Code" Generator that takes text as input and replaces each letter with another letter, and outputs the "encoded" message.
code = input('Enter a message to be encoded>>>')
key = input('Which characters to encode>>>')
encoder = input('With which character do you want to encode?>>>')
print('\n')
print(f"All '{key}'s will be replaced by '{encoder}'s.\n")
print("Encoded message:",code.replace(key,encoder))
decode = input('Do you want to decode the message? (Y)es or (N)o>>>').lower()

if decode == 'y':
    print("Decoded message:", code)
elif decode == 'n':
    print("Understandable. Have a nice day.")
print("Hope you enjoyed using the encoder!")