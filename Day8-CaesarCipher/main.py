import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# original encrypt
def encrypt(plain_text, shift_amt):
    cipher_text = ""
    for letter in plain_text:
        alpha_index = alphabet.index(letter)
        alpha_index += shift_amt
        letters = alphabet[alpha_index]
        cipher_text += letters
    print(f"The encoded text is: {cipher_text}")


# original decrypt
def decrypt(plain_text, shift_amt):
    cipher_text = ""
    for letter in plain_text:
        alpha_index = alphabet.index(letter)
        alpha_index -= shift_amt
        letters = alphabet[alpha_index]
        cipher_text += letters
    print(f"The encoded text is: {cipher_text}")


# combination (shorter version)
def caesar(plain_text, shift_amt):
    cipher_text = ""
    for letter in plain_text:
        alpha_index = alphabet.index(letter)
        if direction == "encode":
            alpha_index += shift_amt
        elif direction == "decode":
            alpha_index -= shift_amt
        letters = alphabet[alpha_index]
        cipher_text += letters
    print(f"The {direction}d text is: {cipher_text}")


print(f"{art.logo}\n")
choice = "yes"
while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > 25:
        shift = shift % 25

    caesar(text, shift)
    choice = input("Do you want to go again? Say 'yes' or 'no'.\n")
