alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(entered_text,your_shift,preferred_direction):
  new_text = ""
  if preferred_direction == "decode": 
    your_shift *= -1 
  for letter in entered_text:
    letter_position = alphabet.index(letter)
    new_position = letter_position + your_shift
    new_text += alphabet[new_position]
  print(f"The {preferred_direction}d text is {new_text}")


caesar(entered_text = text, your_shift = shift, preferred_direction = direction)