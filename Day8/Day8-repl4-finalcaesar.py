
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(entered_text,your_shift,preferred_direction):
  end_text = ""
  if preferred_direction == "decode":
    your_shift *= -1
  for char in entered_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + your_shift
      end_text += alphabet[new_position]
    else:
      end_text += (char)
  print(f"Here's the {preferred_direction}d result: {end_text}")


end_game = False
while not end_game:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(entered_text=text,your_shift=shift,preferred_direction=direction)

  shift = shift % 26 #if user enters value more than the numbers of alphabet

  restart_game = input("Would you like to restart? Type 'yes' or 'no'")
  if restart_game == "no":
    end_game = True
    print("Bye")