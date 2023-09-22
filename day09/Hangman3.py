import time
import random
import sys
import datetime
import tkinter as tk


def read_best_score():
    try:
        with open("BestScore.txt", "r") as file:
            line = file.readline().strip()
            if line:
                parts = line.split(" - ")
                if len(parts) == 2:
                   return int(parts[1])
    except FileNotFoundError:
        return None

def write_best_score(best_score):
    with open("BestScore.txt", "w") as file:
        file.write(f"{formatted_date} - {best_score}")

def add_best_score_record(date, best_score):
    with open("BestScore.txt", "a") as file:
        file.write(f"{date} - {best_score}\n")

if len(sys.argv) != 2:
    print("Usage: python hangman.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

def load_words(filename):
   try:
      with open(filename, 'r') as file:
         words = file.read().splitlines()
         return words
   except FileNotFoundError:
      print("Error: File not found")
      sys.exit(1)
   except Exception as e:
      print(f"An error has occured: {e}")
      sys.exit(1)

def choose_random_word(word_list):
   return random.choice(word_list)


word_list = load_words(filename)
word = choose_random_word(word_list)

root = tk.Tk()
root.title("StickGirl")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

print("")


name = input("What's your name? ")
print("Hello ", name," it's time to play")

time.sleep(1)
print("Start guessing....")
time.sleep(1)

guesses = ''
turns = 10
attempts = 0
wrong_guesses = 0
best_score = read_best_score()

while turns > 0:
    guess = input("\nGuess a character: ").lower()
    attempts += 1
                      
    if len(guess) == 1:
     if guess in word:
      guesses += guess
     else:
       turns -= 1
       print("wrong")
       print ("You have", turns, 'more guesses' )
    if guess == word:
        print(f"Victory! the word {word} is correct!")
        time.sleep(1)
        print("GAME OVER")
        break
    if all(char in guesses for char in word):
       print(f"Victory! the word {word} is correct!")
       time.sleep(1)
       print("Game over")
       break
    if guess not in word:
       wrong_guesses += 1
       if wrong_guesses <= 10:
          if (wrong_guesses) == 1:
            head = canvas.create_oval(50, 50, 110, 90, outline="black", fill="pink", width=2)
          if (wrong_guesses) == 2:
            body = canvas.create_line(100, 90, 100, 140, fill="black", width=2)
          if (wrong_guesses) == 3:
            left_leg = canvas.create_line(100, 140, 80, 180, fill="black", width=2)
          if (wrong_guesses) == 4:
            right_leg = canvas.create_line(100, 140, 120, 180, fill="black", width=2)
          if (wrong_guesses) == 5:
            left_arm = canvas.create_line(100, 100, 80, 150, fill="black", width=2, tags="arms")
          if (wrong_guesses) == 6:
            right_arm = canvas.create_line(100, 100, 120, 150, fill="black", width=2, tags="arms")
          if (wrong_guesses) == 7:
            rope = canvas.create_line(100, 10, 100, 100, fill="red", width=6)
          if (wrong_guesses) == 8:
            pole = canvas.create_line(10, 0, 10, 200, fill="Brown", width=6)
          if (wrong_guesses) == 9:
            pole1 = canvas.create_line(0, 10, 170, 10, fill="Brown", width=6)
          if (wrong_guesses) == 10:
           canvas.create_text(100, 170, text="You LOSE! StickGirl is dead", fill="#FF1493", font=("Arial", 12))
           print("You lose")
           time.sleep(1)
           print("GAME OVER")
           root.mainloop() 
           break
    
       

    for char in word:
        if char in guesses:
            print(char, end="")
        else: 
            print(" _ ", end="")
    

if best_score is None or attempts < best_score:
 best_score = attempts
 print(f"Your best score: {attempts}")
 current_date = datetime.datetime.now()
 formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
 add_best_score_record(formatted_date, best_score)
 write_best_score(best_score) 
else: 
 print(f"Your current score: {attempts}")
 print(f"Best score is: {best_score}")
          

