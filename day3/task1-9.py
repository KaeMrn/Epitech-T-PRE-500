Input = input("Enter a string: ")
Input_Lowercase = Input.lower()
search = ["cat", "garden", "mice"]
occurrence = 0

for term in search:
    LR_count = Input_Lowercase.count(term)
    term_reversed = term[::-1]
    RL_count = Input_Lowercase.count(term_reversed)
    occurrence += LR_count + RL_count

print(occurrence)



    

