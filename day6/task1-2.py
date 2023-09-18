import string

s = input("enter a phrase: ")
n = int(input("enter a number"))

#1
def funA(s, n):
    lowercase_count = 0
    for char in s:
        if char.islower():
            lowercase_count += 1
            if lowercase_count >= n:
                return True
    return False

result = funA(s, n)
print(f"My phrase contains at least {n} lowercase letters: {result}")

#2
def funB(s, n):
    upper_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
            if upper_count >= n:
                return True
    return False
result = funB(s, n)
print(f"My phrase contains at least {n} Uppercase letters: {result}")

#3
def funC(s, n):
    char_count = 0
    for _ in s:
     char_count += 1
     if char_count >= n:
        return True
    return False
result = funC(s, n)
print(f"My phrase contains at least {n} characters: {result}")

#4
def funD(s, n):
    special_count = 0
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?`~"
    for char in s:
        if char in special_characters:
            special_count += 1
            if special_count >= n:
                return True
    return False

result = funD(s, n)
print(f"My phrase contains at least {n} special characters: {result}")

#5
def funE(s,n):
 numbers_count = 0
 for char in s:
     if char.isdigit():
         numbers_count += 1 
         if numbers_count >= n:
             return True
 return False
result = funE(s, n)
print(f"My phrase contains at least {n} numbers: {result}")