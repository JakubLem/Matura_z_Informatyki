class Day:
    def __init__(self,date,water):
        self.date = date
        self.water = water

    def __str__(self):
        return f'{self.date, self.water}'

    def toYear(self):
        return int(self.date[0:4])


def ex1(days):
    year = 2008
    resultyear = 2008
    result = 0
    i = 0
    while i < len(days):
        counter = int(0)
        while days[i].toYear() == year and i < len(days):
            i += 1
            counter += int(days[i].water)
            pass
        if counter > result:



    


def main():
    data = open("Rozszerzona/maj2018/2czesc/Dane_PR2/woda.txt", "r", encoding="utf-8").read().splitlines()
    days = list()
    for i in data:
        day = i.split()
        date = day[0]
        water = day[1]
        days.append(Day(date,water))
    
    for i in days:
        print(i.toYear())

    ex_1 = ex1(days)
    print(ex_1)

if __name__ == "__main__":
    main()