# Write function remove_duplicates(text) that keeps each letter only once in a given
# text, thus deleting all subsequent duplicates regardless of case. However, the original
# order of the letters should be preserved.

def remove_duplicates(text):
    result = ''
    letters = set()

    for char in text:
        if not char.lower() in letters:
            letters.add(char.lower())
            result += char
    print(result)
    return result

remove_duplicates("AaFFfhjdFDD")



