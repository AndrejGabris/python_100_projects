from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrpyt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            original_letter_index = alphabet.index(letter)
            new_position = original_letter_index + shift_amount
            while new_position > (len(alphabet) - 1):
                new_position = new_position - len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is: {cipher_text}\n")


def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            moved_letter_index = alphabet.index(letter)
            new_position = moved_letter_index - shift_amount
            while new_position < 0:
                new_position = new_position + len(alphabet)
            original_text += alphabet[new_position]
        else:
            original_text += letter
    print(f"The original text is: {original_text}\n")

end_program = True
while end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrpyt(plain_text=text,shift_amount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text,shift_amount=shift)

    rerun_program = input("Press [y] = yes or [n] = no:\n")
    while not (rerun_program == "y" or rerun_program == "n"):
        rerun_program = input("Press [y] = yes or [n] = no:\n")

    if rerun_program == "n":
        end_program = False

