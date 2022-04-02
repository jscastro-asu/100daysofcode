'''Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name = name1.lower()
second_name = name2.lower()

count_t = first_name.count("t") + second_name.count("t")
count_r = first_name.count("r") + second_name.count("r")
count_u = first_name.count("u") + second_name.count("u")
count_e = first_name.count("e") + second_name.count("e")
true = (count_t + count_r + count_u + count_e)
lover = str(true)

count_l = first_name.count("l") + second_name.count("l")
count_o = first_name.count("o") + second_name.count("o")
count_v = first_name.count("v") + second_name.count("v")
count_e2 = first_name.count("e") + second_name.count("e")
love = (count_l + count_o + count_v + count_e2)
score = str(love)

final_score = int(lover + score)

if 40 <= final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")

elif final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {final_score}")
        
