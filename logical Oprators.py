# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:50:27 2023

@author: Web 123
"""

# Question 1
# Write code that asks the user to input a number between 1 and 5 inclusive.
# The code will take the integer value and print out the string value. So for
# example if the user inputs 2 the code will print two. Reject any input that
# is not a number in that range

# n1 = int(input('Enter The number In Range 1-5 '))
# if n1 == 1 :
#     print('You Enter The Number One')
# elif n1 == 2 :
#       print('You Enter The Number Two')
# elif n1 == 3 :
#       print('You Enter The Number Three')
# elif n1 == 4 :
#       print('You Enter The Number Four')
# elif n1 == 5 :
#       print('You Enter The Number Five')
# else:
#       print('You Have Enter Out Of Range Numbers')

# Question 2
# Repeat the previous task but this time the user will input a string and the
# code will ouput the integer value. Convert the string to lowercase first.

# n1 = input('Enter The number In Range One to Five In Lower case >> ')
# if n1 == 'one' :
#     print('You Enter The Number 1')
# elif n1 == 'two' :
#       print('You Enter The Number 2')
# elif n1 == 'three':
#       print('You Enter The Number 3')
# elif n1 == 'four' :
#       print('You Enter The Number 4')
# elif n1 == 'five':
#       print('You Enter The Number 5')
# else:
#       print('You Have Enter Out Of Range Numbers')

# Question 3
# Create a variable containing an integer between 1 and 10 inclusive. Ask the
# user to guess the number. If they guess too high or too low, tell them they
# have not won. Tell them they win if they guess the correct number.

secret_number=5
guess=input('Guess The secrate number in 1-10 >>')
if guess.isdigit():
      guess = int(guess)
      if guess == secret_number:
        print('you Guessed the Secrate Number''You Win!')
      elif guess > secret_number and guess <= 10 :
    
        print('you Guessed too High ''Sorry you Lose!')
      elif guess < secret_number and guess >= 1 :  
   
        print('You Guessed too Low ''Sorry You Lose!')
      else:
        print('Out of range')
else:
    print('That\'s Not even an Integer ! what are you Playing at ?!')   


# secret_number = 3
# guess = input('Guess the number between 1-10:> ')
# if guess.isdigit():
#     guess = int(guess)
#     if guess == secret_number:
#         print('You guessed the correct number! You win!')
#     elif guess > secret_number and guess <= 10:
#         print('You guessed too high. Sorry you lose!')
#     elif guess < secret_number and guess >= 1:
#         print('You guessed too low. Sorry you lose!')
#     else:
#         print('Out of range')
# else:
#     print('That\'s not even an integer! What are you playing at?!')

     
        