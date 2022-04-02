alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(your_text,your_shift):

    cipher_text = ""
    for each_letter in your_text:
      letter_position = alphabet.index(each_letter)
      new_position = letter_position + your_shift
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, your_shift):

  decipher_text = ""
  for each_letter in cipher_text:
    letter_position = alphabet.index(each_letter)
    new_position = letter_position - your_shift
    new_letter = alphabet[new_position]
    decipher_text += new_letter
  print(f"The decoded text is {decipher_text}")


if direction == "encode":
  encrypt(your_text=text, your_shift=shift)
elif direction == "decode":
  decrypt(cipher_text=text, your_shift=shift)