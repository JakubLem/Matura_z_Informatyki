import math

def ex1(rows):
    result = str("")
    for i in range(39,len(rows),40):
        result += rows[i][9]
    return result

def ex2(rows):
    word = str()
    maincounter = int(0)
    for i in rows:
        counter = int(0)
        charlist = list()
        for char in i:
            if char not in charlist:
                counter += 1
                charlist.append(char)
        if counter > maincounter:
            maincounter = counter
            word = i
    return {'word' : word, 'counter' : maincounter}

def wordCheck(word):
    char = word[0]
    for i in range(1,len(word),1):
        if abs(ord(word[i-1])-ord(word[i])) > 10:
            return False
    return True

def ex3(rows):
    result = list()
    for word in rows:
        if wordCheck(word):
            result.append(word)
    return result



def main():
    rows = open("Rozszerzona/maj2018/2czesc/Dane_PR2/sygnaly.txt", "r", encoding="utf-8").read().splitlines()
    ex_1 = ex1(rows)
    print(ex_1)
    ex_2 = ex2(rows)
    print(ex_2)
    ex_3 = ex3(rows)
    print(ex_3)


if __name__ == "__main__":
    main()