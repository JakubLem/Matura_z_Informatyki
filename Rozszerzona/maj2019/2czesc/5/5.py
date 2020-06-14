def splitToTab(line):
    return line.replace(";"," ").split()


class Day:
    def __init__(self,dzien,temperatura,opad,kat_chmur,wiel_chmur):
        self.dzien = int(dzien)
        self.temperatura = float(temperatura.replace(",","."))
        self.opad = int(opad) 
        self.kat_chmur = str(kat_chmur)
        self.wiel_chmur = int(wiel_chmur)

    def __str__(self):
        return f'{self.dzien, self.temperatura, self.opad, self.kat_chmur, self.wiel_chmur}'

def ex1(days):
    counter = int(0)
    for i in days:
        if float(i.temperatura) >= float(20) and int(i.opad) <= int(5):
            counter+=1
    return counter

def ex2(days):
    result = list()
    i = 0
    while i < len(days)-1:
        counter = list()
        temp = days[i].temperatura
        i+=1
        while days[i].temperatura > temp:
            temp = days[i].temperatura
            counter.append(days[i])
            i+=1
            if i==len(days):
                break
        if len(counter)>len(result):
            result = counter
        i+=1

    for i in result:
        print(i)
    return {result[0].dzien, result[len(result)-1].dzien}

def ex3(days):
    class Type:
        def __init__(self):
            self.sum = float(0.0)
            self.counter = int(0)
            self.avarage = float(0.0)

        def setAvarage(self):
            self.avarage = float(float(self.sum)/float(self.counter))

        def addDay(day):
            self.sum += float(day.opad)
            self.counter += 1

    c1 = Type()
    c2 = Type()
    c3 = Type()
    c4 = Type()
    c5 = Type()
    s1 = Type()
    s2 = Type()
    s3 = Type()
    s4 = Type()
    s5 = Type()

    for i in range(0,300,1):
        pass

def main():
    data = open('Rozszerzona/maj2019/2czesc/Dane_PR2/pogoda.txt','r',encoding='utf-8').read().splitlines()
    days = list()
    for i in range(1,len(data),1):
        tab = splitToTab(data[i])
        days.append(Day(tab[0],tab[1],tab[2],tab[3],tab[4]))
        """print(days[i-1])
        ex = input()"""
    
    
    first_ex = ex1(days)
    print(first_ex)
    second_ex = ex2(days)
    print(second_ex)
    startDay, stopDay = second_ex
    print(startDay)
    print(stopDay)

if __name__ == "__main__":
    main()