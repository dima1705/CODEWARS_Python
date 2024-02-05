def to_jaden_case(string):
    setaq = ''
    for i in string.split(' '):
        i = i.capitalize() + ' '
        setaq += i

    return setaq[:-1] == "How Can Mirrors Be Real If Our Eyes Aren't Real"


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))