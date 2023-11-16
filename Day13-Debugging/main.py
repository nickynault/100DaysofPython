# DEBUGGING
# Mostly today was just messing around with debugging, not an actual project.

# # Describe Problem
# def my_function():
#   for i in range(1, 20):           change 20 -> 21, to fix the range / i issue.
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_img = ["❶", "❷", "❸", "❹", "❺", "❻"]     spamming run here eventually gives an IndexError for the last line (list out of range)
# dice_num = randint(1, 6)                        6 is not in the range (it's 0-5, not 1-6), so making it choose 6 only breaks it EVERY time.
# print(dice_img[dice_num])                       so the issue shows up here, since it occurs when printing, but the issue is obviously the previous line.

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millennial.")
# elif year > 1994:                   none of the code block accounts for 1994 as an entry. either add >= here or <= 2 lines above.
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")            not transforming the inout here will cause an error below. we ask for an int, but of course, get a string.
# if age > 18:
# print("You can drive at age {age}.")        We get an error here because of the int and strings, but ALSO need to use an f string to throw a variable into a print statement.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))    "==" here is not right. need '='.
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)            Using a debugger we can see that it loops, then AFTER the loop, adds the value. If we want ALL the values, add
#   print(b_list)                      the append statement into the for loop.

# mutate([1,2,3,5,8,13])
