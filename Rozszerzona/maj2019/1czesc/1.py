def ex1(tab):
    if tab[0]%2==0:
        return tab[0]
    for i in range(len(tab)-1,1,-1):
        if tab[i]%2!=0:
            return tab[i+1]

def ex2(tab):
    pass


def main():
    A = [99, 3, 7, 111, 13, 4, 24, 4, 8]
    print(ex1(A))
    print("NIE KURWA")

if __name__ == "__main__":
    main()
    