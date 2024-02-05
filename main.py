def smash(words):
    sentence = ''
    for i in words:
        sentence += i
        sentence += ' '

    return f"{sentence[:-1]}"


smash(['hello', 'world', 'this', 'is', 'great'])