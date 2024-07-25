word = input("Enter word :")

vowel = ''
consonant = ''

for character in word:
	if character.lower() in ['a', 'e', 'i', 'o', 'u' ]:
		vowel += character
	else:
		consonant += character

print(f"The number of vowels {len(vowel), set(vowel) , vowel}")
print(f"The number of consonant {len(consonant), set(consonant) , consonant}")
