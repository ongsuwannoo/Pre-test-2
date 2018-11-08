""" Digital Clock """
def main():
    """ input """
    h_24 = int(input())
    m_60 = int(input())
    if (0 <= h_24 < 24) and (0 <= m_60 <= 59):
        if h_24 < 12:
            print("%d:%02d AM"%(h_24, m_60))
        elif h_24 == 12:
            print("%d:%02d PM"%(h_24, m_60))
        else:
            h_24 -= 12
            print("%d:%02d PM"%(h_24, m_60))
    else:
        print("Invalid Time")

main()
