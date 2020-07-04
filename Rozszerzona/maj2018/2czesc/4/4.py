

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
            if char is not in charlist:
                counter += 1
                charlist.append(char)
        if counter > maincounter:
            maincounter = counter
            word = i
    return {'word' : word, 'counter' : maincounter}

def ex3(rows):
    pass



def main():
    rows = open("Rozszerzona/maj2018/2czesc/Dane_PR2/sygnaly.txt", "r", encoding="utf-8").read().splitlines()
    ex_1 = ex1(rows)
    print(ex_1)


if __name__ == "__main__":
    main()