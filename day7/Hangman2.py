import time

name = input("What's your name? ")
print("Hello ", name," it's time to play")

time.sleep(1)
print("Start guessing....")
time.sleep(1)

word = ("love")
guesses = ''
turns = 10

while turns > 0:
    guess = input("\nGuess a character: ").lower()
                      
    if len(guess) == 1:
     if guess in word:
      guesses += guess
     else:
       turns -= 1
       print("wrong")
       print ("You have", turns, 'more guesses' )
    if guess == word:
        print("Victory!")
        time.sleep(1)
        print("GAME OVER")
        break
    if turns == 0:
       print("You lose")
       time.sleep(1)
       print("GAME OVER")
       break

    for char in word:
        if char in guesses:
            print(char, end="")
        else: 
            print(" _ ", end="")
