import string

input_string = input("say something: ")
input_string = input_string.lower()

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

def palindrome(input_string):
    if len(input_string) <= 1:
     return True
    
    if input_string[0] != input_string[-1]:
       return False
    
    return palindrome(input_string[1:-1])
    
result = palindrome(input_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
