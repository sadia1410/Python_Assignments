# -*- coding: utf-8 -*-
"""GIAIC PYTHON.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IWJhzKtbqE5I3magCT9BVoEEpqbDb89G

# ***Mad libs Python Project***
"""

database = []
name = input("Enter your name: ")
age = float(input("Enter your age: "))
database.append(name)
database.append(age)
print(f"Dear student your name:{name} and your age:{age} is submitted successfully in our database")

"""# ***Guess the Number Game Python Project (computer)***"""

import random as r
def guess_number(num1,num2):
  generated_number = r.randint(1,100)
  print(f"wining number is: {generated_number}")
  while True:
    if num1 == generated_number:
      print("You win the game")
      break
    elif num2 == generated_number:
      print("You win the game")
      break
    else:
      print("You lose the game")
      break
user1 = int(input("Enter the first number: "))
user2 = int(input("Enter the second number: "))
guess_number(user1,user2)

"""# ***Guess the Number Game Python Project (user)***"""

import random as r
print("🎯 Welcome to Guess the Number!\n")
def guess_number(num1):
  generated_number = r.randint(1,100)
  print(f"wining number is: {generated_number}")
  while True:
    if num1 == generated_number:
      print("You win the game")
      break
    else:
      print("You lose the game")
      break
user1 = int(input("Enter the first number: "))
guess_number(user1)

"""# ***Rock, paper, scissors Python Project***"""

import random as r
data = ["rock", "paper", "scissors"]

def user():
  user_input = input("Enter rock, paper, or scissors: ")
  if user_input not in data:
    print("invalid")
    return user()
  return user_input
def computer():
  computer_input = r.choice(data)
  return computer_input

def winner(user_input,computer_input):
  print(f"Your choice is: {user_input}")
  print(f"computer choice is: {computer_input}")

  winner = r.choice(data)
  if user_input == computer_input:
    print("tie")
    print(f"winner is : {winner}")


  elif user_input == "rock" and computer_input == "scissors":
    winner = "user"
    print(f"winner is : {winner}")


  elif user_input == "paper" and computer_input == "rock":
    winner = "user"
    print(f"winner is : {winner}")


  elif user_input == "scissors" and computer_input == "paper":
    winner = "user"
    print(f"winner is : {winner}")


  else:
    winner = "computer"
    print(f"winner is : {winner}")


user()
computer()
winner(user(),computer())

"""# ***Hangman Python Project***"""

import random

# List of words
word_list = ["python", "hangman", "coding", "developer", "project", "function", "variable", "streamlit"]

def get_random_word(word_list):
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word(word_list)
    guessed_letters = []
    tries = 6  # Number of wrong attempts allowed

    print("🎉 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⛔ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            tries -= 1
            print(f"❌ Wrong guess! Tries left: {tries}")

        print(display_word(word, guessed_letters))

        # Check for win
        if all(letter in guessed_letters for letter in word):
            print("🎉 You won! The word was:", word)
            break

    else:
        print("💀 Game over! The word was:", word)

# Start the game
if __name__ == "__main__":
    hangman()

"""# ***Countdown Timer Python Project***"""

import time

# Ask the user for input
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert total time to seconds
total_seconds = minutes * 60 + seconds

# Countdown loop
while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)
    timer = f'{mins:02d}:{secs:02d}'
    print("⏳", timer, end="\r")  # \r keeps it on the same line
    time.sleep(1)
    total_seconds -= 1

# Time is up!
print("⏰ Time's up!             ")

"""# ***Password Generator Python Project***"""

import random
import string

# Ask the user how long the password should be
length = int(input("Enter the desired password length: "))

# Define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation
# ascii_letters = a-z + A-Z
# digits = 0-9
# punctuation = !@#$%^&*(), etc.

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

print("Generated password:", password)