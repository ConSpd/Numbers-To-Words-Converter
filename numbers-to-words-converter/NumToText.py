def tens(f):
    if f == "11":
        return "eleven"
    elif f == "12":
        return "twelve"
    elif f == "13":
        return "thirteen"
    elif f == "14":
        return "fourteen"
    elif f == "15":
        return "fifteen"
    elif f == "16":
        return "sixteen"
    elif f == "17":
        return "seventeen"
    elif f == "18":
        return "eighteen"
    elif f == "19":
        return "nineteen"

    elif f[0] == "2":
        return "twenty"
    elif f[0] == "3":
        return "thirty"
    elif f[0] == "4":
        return "forty"
    elif f[0] == "5":
        return "fifty"
    elif f[0] == "6":
        return "sixty"
    elif f[0] == "7":
        return "seventy"
    elif f[0] == "8":
        return "eighty"
    elif f[0] == "9":
        return "ninety"
    else:
        return ""


def ones(f):
    if f == "1":
        return "one"
    elif f == "2":
        return "two"
    elif f == "3":
        return "three"
    elif f == "4":
        return "four"
    elif f == "5":
        return "five"
    elif f == "6":
        return "six"
    elif f == "7":
        return "seven"
    elif f == "8":
        return "eight"
    elif f == "9":
        return "nine"
    else:
        return ""


def divide_triads(f):  # Divide number into triplets i.e. 1234567 turns into ['567','234','1']
    sets = [""]
    p = 0
    j = 0
    for i in reversed(range(len(f))):  # We reverse the string to find where the separator dots are placed
        sets[p] = f[i] + sets[p]
        j += 1
        if j % 3 == 0 and i > 0:
            sets.append("")
            p += 1
    return sets


def hundreds(f):  # Function gets a triad as input. Triad may be from 1 to 3 numbers. The function prints the range 0-999
    msg = ""
    if len(f) == 1 and f == "0":
        msg = "zero"
        return msg

    if f[0] == "0":  # 023
        f = f[1:]

    if len(f) % 3 == 0:  # 123
        msg += ones(f[0]) + " "
        msg += "hundred "
        f = f[1:]

    if len(f) % 2 == 0:  # 23
        msg += tens(f[0:2]) + " "
        if f[0] == "1":
            f = f[2:]
        else:
            f = f[1:]

    if len(f) > 0 and f[0] != "0":
        msg += ones(f[0]) + " "

    return msg


def validate_input(f):
    if len(f) == 0:
        raise Exception("Input can't be empty")
    if len(f) > 27:
        raise Exception("Input can't surpass 27 digits")
    if not f.isnumeric():
        raise Exception("Input should contain only digits")
    if f[0] == '0' and len(f) > 1:
        raise Exception("First digit can't be zero")


def num_to_text(f):
    validate_input(f)
    number = divide_triads(f)
    msg = ""
    while len(number) > 0:
        triad = number[len(number)-1]

        if triad == "00" or triad == "000":
            number.pop()
            continue

        msg += hundreds(triad)
        if len(number) == 2:
            msg += "thousand "
        elif len(number) == 3:
            msg += "million "
        elif len(number) == 4:
            msg += "billion "
        elif len(number) == 5:
            msg += "trillion "
        elif len(number) == 6:
            msg += "quadrillion "
        elif len(number) == 7:
            msg += "quintillion "
        elif len(number) == 8:
            msg += "sextillion "
        elif len(number) == 9:
            msg += "septillion "
        number.pop()
    return msg


def main():
    f = input("Give number: ")
    f_n = num_to_text(f)
    print(f_n)


if __name__ == '__main__':
    main()
