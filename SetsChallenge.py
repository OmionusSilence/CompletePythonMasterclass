# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = input("Input some text to find non vowels of: ").strip().lower()
vowels = {"a", "e", "i", "o", "u"}

textSet = set(text)

textSet.difference_update(vowels)

print("Non vowels in text are: ", sorted(textSet))
