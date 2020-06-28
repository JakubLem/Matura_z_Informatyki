class Row:
    def __init__(self,number,word):
        self.number = number
        self.word = word
        self.goldbach = list()
        self.frag = str("")
        self.frag_counter = 0

    def __str__(self):
        goldbach = str("")
        if len(self.goldbach)!=0:
            goldbach = str("[" + str(self.goldbach[0][0]) + str(" , ") + str(self.goldbach[0][1]) + "]") 
        return f'{self.number, self.word, goldbach, self.frag, self.frag_counter}'

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

def ex2(rows):
    for i in rows:
        array = list(i.word)
        index = int(0)
        result = int(0)
        char = str("")
        c = array[0]
        while index < len(array)-1:
            index += 1
            counter = int(1)
            while c == array[index]:
                index += 1
                counter += 1
                if index == len(array):
                    break
            if counter > result:
                result = counter
                char = c
            if index != len(array):
                c = array[index]
        i.frag = char
        i.frag_counter = result

    return rows




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

    rows = ex2(rows)

    for i in rows:
        print(i)

    

if __name__ == "__main__":
    main()