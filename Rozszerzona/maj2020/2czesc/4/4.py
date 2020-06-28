class Row:
    def __init__(self,number,word):
        self.number = number
        self.word = word

    def __str__(self):
        return f'{self.number, self.word}'



def ex1(rows):
    pass

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
    
    ex_1 = ex1(rows)

if __name__ == "__main__":
    main()