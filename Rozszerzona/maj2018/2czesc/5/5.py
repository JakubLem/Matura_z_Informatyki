class Day:
    def __init__(self,date,water):
        self.date = date
        self.water = water

    def __str__(self):
        return f'{self.date, self.water}'


def ex1():
    pass

def main():
    data = open("Rozszerzona/maj2018/2czesc/Dane_PR2/woda.txt", "r", encoding="utf-8").read().splitlines()
    days = list()
    for i in data:
        day = i.split()
        date = day[0]
        water = day[1]

        print(i.split())
    

if __name__ == "__main__":
    main()