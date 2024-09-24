from telnetlib import theNULL


def classwork(user):
    letter_dict = {}
    for letter in user:
        letter_count = 0
        for the_letter in user:
            if letter == the_letter:
                letter_count+= 1
        letter_dict[letter] = letter_count
    return letter_dict
print (classwork("AAAAJJEKDoele"))














