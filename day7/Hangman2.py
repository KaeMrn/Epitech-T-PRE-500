import time

name = input("What's your name?")
print("Hello ", name," it's time to play")

time.sleep(1)
print("Start guessing....")
time.sleep(1)

word = ("love")
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else: 
            print(" _ ", end="")
            failed += 1
    if failed == 0:
        print("Victory!")
        break
    guess = input("Guess a character: ")
    if len(guess) == 1:
     guesses += guess
     if guesses not in word:
       turns -= 1
       print("wrong")
       print ("You have", + turns, 'more guesses' )
    if guess == word:
        print("Victory!")
        break
    if turns == 0:
       print("You lose")
       break
