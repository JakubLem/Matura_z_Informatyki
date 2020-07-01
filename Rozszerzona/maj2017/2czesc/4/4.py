
class Transaction:
    def __init__(self, date, nip, weight):
        self.date = date
        self.nip = nip
        self.weight = weight

    def __str__(self):
        return f'{self.date, self.nip, self.weight}'

class PriceList:
    def __init__(self,year,price):
        self.year = year
        self.price = price

    def __str__(self):
        return f'{self.year, self.price}'

def ex1():
    pass


def main():
    transactions = list()
    data = open("Rozszerzona/maj2017/2czesc/Dane_PR2/cukier.txt", "r", encoding="utf-8").read().splitlines()
    for i in data:
        row = i.split()
        date = row[0]
        nip = row[1]
        weight = row[2]
        transactions.append(Transaction(date=date, nip=nip, weight=weight)) 

    pricelist = list()
    data = open("Rozszerzona/maj2017/2czesc/Dane_PR2/cennik.txt", "r", encoding="utf-8").read().splitlines()
    for i in data:
        row = i.split()
        pricelist.append(PriceList(row[0], row[1]))
    
    for i in pricelist:
        print(i)

if __name__ == "__main__":
    main()