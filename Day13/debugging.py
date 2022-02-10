############DEBUGGING#####################

# # Describe Problem

#bug
# def my_function():
#    for i in range(1, 20):
#      print(i)
#      if i == 20:
#        print("You got it")
# my_function()

#my solution - unable to print you got it because in range start is a 0 (included), so if you print range it gives you only 1-19"""
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug

# bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

#my solution - index starts with [0, error out of range because there is no 6 in the set, it is 0-5]"""

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer

#bug
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


# my solution - when you type 1994 nothing happens so you have to include <= 1994 so the millenial condition applies"""

# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# bug
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

#my solution - tab"""
# age = input("How old are you?")
# if age > 18:
#   print("You can drive at age {age}.")

# #Print is Your Friend

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#The issue here is the ==, since it is setting itself whatever the input will be"""

#bug
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#pythontutor.com
#my solution: in order for it to print the entire b_list and not just [26] """

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])