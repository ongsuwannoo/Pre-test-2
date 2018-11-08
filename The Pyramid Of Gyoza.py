""" The Pyramid Of Gyoza """
def main():
    """ input """
    num = int(input())
    for _ in range(1, num+1):
        print(" " * (num - _) + "*" * (_ + _ - 1))

main()
