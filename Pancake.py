""" Pancake """
def main():
    """ input """
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = 0
    num5 = 0
    num6 = 0
    total = 0
    if num1 > num3:
        print("Pay: %d"%(num3*20))
        while num6 < num3:
            num6 += 1
        print("Get: %d"%(num6))
    elif num1 <= num3:
        if (num1+num2) > num3:
            print("Pay: %d"%(num1*20))
            print("Get: %d"%(num1+num2))
        else:
            while total < num3:
                total += 1
                num4 += 1
                num5 += 1
                if num4 == num1:
                    total += num2
                    num4 = 0
            print("Pay: %d"%(num5*20))
            print("Get: %d"%(total))

main()
