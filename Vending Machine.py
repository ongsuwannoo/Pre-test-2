""" Vending Machine """
def main():
    """ input """
    num = ""
    money = 0
    item = 0
    cost = 0
    while True:
        num = input()
        if num == "END":
            break
        else:
            num = int(num)
        if num >= 0:
            money += num
        elif num < 0:
            cost = num + money
            if cost < 0:
                print("ERROR: Not enough money for this item.")
            else:
                item += 1
                money += num
    print("Items: %d"%(item))
    print("Change: %d THB"%(money))

main()
