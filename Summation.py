""" Summation """
def main():
    """ input """
    num = int(input())
    result = 0
    for _ in range(1, num+1):
        num1 = float(input())
        result += num1
    print("%.4f"%(result))

main()
