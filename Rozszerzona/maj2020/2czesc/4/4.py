class Row:
    def __init__(self,number,word):
        self.number = number
        self.word = word
        self.goldbach = list()

    def __str__(self):
        goldbach = str("")
        if len(self.goldbach)!=0:
            for i in self.goldbach:
                goldbach += str("[" + str(i[0]) + "," + str(i[1]) + "]") 
        return f'{self.number, self.word, goldbach}'

def pierwsza(n):
    if n == 0 or n == 1:
        return False
    p = int(2)
    while p!=n:
        if n%p==0:
            return False
        p += 1
    return True

def ex1(rows):
    for i in rows:
        num = i.number
        if num > 4:
            for x in range(num):
                if pierwsza(x) == True: 
                    for y in range(num-x+1):
                        if pierwsza(y) == True:
                            if x+y == num:
                                i.goldbach.append([x,y])
                                continue
    return rows

def ex2():
    pass

def ex3():
    pass


def getRows(path):
    rows = list()
    data = open(path, "r", encoding="utf-8").read().splitlines()
    for i in data:
        obj = i.split()
        rows.append(Row(int(obj[0]),obj[1]))
    return rows

def main():
    rows = getRows("Rozszerzona/maj2020/2czesc/Dane_PR2/pary.txt")
    
    rows = ex1(rows)

    for i in rows:
        print(i)

    print(pierwsza(5))

if __name__ == "__main__":
    main()