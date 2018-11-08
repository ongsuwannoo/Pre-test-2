""" Alphabet Sequence """
def main():
    """ input """
    cha = ord(input())
    nub = 65
    cha2 = 65
    while nub <= cha:
        print(chr(cha2), end="")
        cha2 += 1
        nub += 1
        if cha2 == 91:
            cha2 = 97
            nub = 97

main()
