def splitToTab(line):
    return line.replace(";"," ").split()


class Day:
    def __init__(self,dzien,temperatura,opad,kat_chmur,wiel_chmur):
        self.dzien = dzien
        self.temperatura = temperatura
        self.opad = opad 
        self.kat_chum = kat_chmur
        self.wiel_chmur = wiel_chmur

    def __str__(self):
        return f'{self.dzien, self.temperatura, self.opad, self.kat_chmur, self.wiel_chmur}'

def ex1(days):
    pass



def main():
    data = open('Rozszerzona/maj2019/2czesc/Dane_PR2/pogoda.txt','r',encoding='utf-8').read().splitlines()
    days = list()
    for i in data:
        tab = splitToTab(i)
        days.append(Day(tab[0],tab[1],tab[2],tab[3],tab[4]))
    print(days)
    

if __name__ == "__main__":
    main()