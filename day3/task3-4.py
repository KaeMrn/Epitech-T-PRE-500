import re
text = input("Please enter a text with multiple sentences: ")# Get the input text from the user

sentences = re.split(r'[.!?]', text)
first_words = []

for sentence in sentences:
    words = sentence.split()
    if words:
            first_word = words[0]
            first_words.append(first_word)
    new_sentence = ' '.join(first_words)

print("Resulting sentence:", new_sentence)
