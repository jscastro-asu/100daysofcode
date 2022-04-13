#Generate new text file for each person from a list. Replace the template placeholder with the name.
with open("./Input/Names/invited_names.txt", "r") as names:
    namelist = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    invitation = letter.read()
    for n in namelist:
        strip_names = n.strip()
        new_letter = invitation.replace("[name]", strip_names)
        with open(f"./Output/ReadyToSend/invite_for_{strip_names}.txt", "w") as send_letter:
            send_letter.write(new_letter)



     
  

