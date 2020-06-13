import math





def ex1():

    def ispower(el):
        number = 1
        while number<el:
            number*=3
        if number == el:
            return True
        return False

    data = open("Rozszerzona/maj2019/2czesc/Dane_PR2/liczby.txt","r", encoding="utf-8").read().splitlines()
    result = list()

    for i in data:
        if ispower(int(i)):
            result.append(i)
    return result


def ex2():
    def silnia(n):
        if n==0 or n==1:
            return 1
        res = 1 
        for i in range(1,n+1,1):
            res*=i
        return res


    data = open("Rozszerzona/maj2019/2czesc/Dane_PR2/liczby.txt","r", encoding="utf-8").read().splitlines()
    result = list()

    for i in data:
        summary = int(0)
        for x in list(i):
            summary += silnia(int(x))
        if int(summary) == int(i):
            result.append(i)
    return result

    

def main():
    # print(len(ex1()))
     print(ex2())

if __name__ == "__main__":
    main()