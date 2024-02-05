def xo(string):
    return True if string.lower().count('x') == string.lower().count('o') else False


print(xo('zzoo'))