#1- Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  new = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return new

print(password_generator("Reiko", "Matsuki"))

#2- Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
print(second_to_last)

#3- Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.
final_word = company_motto[-4:]
print(final_word)

#4 Write a function called letter_check that takes two inputs, word and letter.This function should return True if the word contains the letter and False if it does not.
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
letter_check("strawberry", "a")

#5- concatenate the string "R" with a slice of first_name that includes everything but the first character, "B", and save it to a new string fixed_first_name.
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R"+first_name[1:]

#6 Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string. For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False
print(contains("watermelon", "berry"))

#7 Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

#The letters in the returned list should be unique. For example,common_letters("banana", "cream")should return ['a'].
ef common_letters(string_one, string_two):
  contains_yes = []
  for letter in string_one:
    if letter in string_two and letter not in contains_yes:
      contains_yes.append(letter) 
  return contains_yes

print(common_letters("banana", "bacon"))

#8 the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

# by defining the function password_generator so that it takes one input, username and in it define an empty string named password.

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
  #9Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

#To shift the letters right, at each letter the for loop should add the previous letter to the string password.
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
  
  
