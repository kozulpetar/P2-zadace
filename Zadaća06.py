def unazad(string):
    if len(string) <= 1:
        return string
    else:
        return unazad(string[1:]) + string[0]

print(unazad("programiranje"))