# Write a function that takes in a string of one or more words,
# and returns the same string, but with all words that have five
# or more letters reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:
# "Hey fellow warriors" --> "Hey wollef sroirraw"
# "This is a test --> "This is a test"
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    sentence_list = sentence.split(' ')
    result = [word[::-1] if len(word) >= 5 else word for word in sentence_list]
    return ' '.join(result)


# Tests
assert spin_words("Welcome") == "emocleW"
assert spin_words("to") == "to"
assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
