""" Spear """
def main():
    """ input """
    num = int(input())
    num2 = 4
    num1 = 1
    print(" " * (num//2) + "*")
    if num > 1:
        for i in range(1, num//2+1):
            print(" " * (num // 2 - i) + ("*" + (" " * (i + i - 1)) + ("*")))
        while num1 < num//2:
            print(" " * num1 + "*" + " " * (num - num2) + "*")
            num1 += 1
            num2 += 2
        print(" " * (num//2) + "*")
    for _ in range(1, num + 1):
        print(" " * (num // 2) + "*")

main()
