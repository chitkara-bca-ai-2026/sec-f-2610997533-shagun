sentence = input("Enter a sentence: ")

words = sentence.split()
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for character in sentence:
    if character.lower() in "aeiou":
        vowels = vowels + 1
    elif character.isalpha():
        consonants = consonants + 1
    elif character.isdigit():
        digits = digits + 1
    elif character == " ":
        spaces = spaces + 1
    else:
        special_characters = special_characters + 1

total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("\n--- DOCUMENT ANALYSIS REPORT ---")
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")
print("Words:", len(words))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)

print("\n--- Summary ---")
print("Total letters:", total_letters)
print("Vowel percentage:", round(vowel_percentage, 1), "%")