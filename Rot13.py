"""
DESCRIPTION:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


import string


def rot13(message):

    new_message = ''

    for i in message:
        if i == ' ':
            new_message += i
            continue

        elif i in string.ascii_lowercase:

            ### for lowerCase letters

            i = string.ascii_lowercase.find(i)
            try:
                new_message += string.ascii_lowercase[i + 13]
            except IndexError:
                i += 13
                new_message += string.ascii_letters[i - 26]
        elif i in string.ascii_uppercase:

            ### for upperCase letters

            i = string.ascii_uppercase.find(i)
            try:
                new_message += string.ascii_uppercase[i + 13]
            except IndexError:
                i += 13
                new_message += string.ascii_uppercase[i - 26]

        else:
            new_message += i

    return new_message


print(rot13('Test'))


