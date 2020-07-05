class Day:
    def __init__(self,date,water):
        self.date = date
        self.water = water

    def __str__(self):
        return f'{self.date, self.water}'

    def toYear(self):
        return int(self.date[0:4])

    def getMonth(self):
        return int(self.date[5:7])


def ex1(days):
    year = 2008
    resultyear = 2008
    result = 0
    i = 0
    while i < len(days):
        counter = int(0)
        while days[i].toYear() == year:
            counter += int(days[i].water)
            i += 1
            if i == len(days):
                break
        if counter > result:
            resultyear = year
            result = counter
        i += 1
        year += 1
    return resultyear

def ex2(days):
    i = 0
    reslen = 0
    while i < len(days):
        singlelen = 0
        startDate = days[i].date
        while int(days[i].water) > 10000:
            i += 1
            singlelen += 1
        if singlelen > reslen:
            date = {'startDate': startDate, 'stopDate': days[i-1].date}
            reslen = singlelen
        i += 1
    return date
        
def ex3(days):
    months = list()
    i = 0
    month = 1
    while days[i].toYear() == 2008:
        water = int(0)
        while days[i].getMonth() == month:
            water += int(days[i].water)
            i += 1
        months.append({'month': month , 'water': water})
        month += 1
        if month == 13:
            return months

         



    


def main():
    data = open("Rozszerzona/maj2018/2czesc/Dane_PR2/woda.txt", "r", encoding="utf-8").read().splitlines()
    days = list()
    for i in data:
        day = i.split()
        date = day[0]
        water = day[1]
        days.append(Day(date,water))
    

    ex_1 = ex1(days)
    print(ex_1)

    ex_2 = ex2(days)
    print(ex_2)

    ex_3 = ex3(days)
    print(ex_3)

if __name__ == "__main__":
    main()