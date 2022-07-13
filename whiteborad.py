# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’


from os import remove


def vowel(word):
    new_word = list(word)
    aeiou = ["a", "e", "i", "o", "u"]
    for y in new_word:
        if y in aeiou:
           word = word.replace(y, "")
            
    return word
print(vowel("Joel"))


        