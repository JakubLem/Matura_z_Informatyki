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
        self.summaryWeight = int(0)

    def __str__(self):
        return f'{self.year, self.price, self.summaryWeight}'


class Client:
    def __init__(self,nip):
        self.nip = nip
        self.sugarWeight = int(0)

    def __str__(self):
        return f'{self.nip, self.sugarWeight}'

    def addSugar(self,weight):
        self.sugarWeight += weight


def getCost(pricelist, year):
    for i in pricelist:
        if str(i.year) == str(year):
            return float(round(float(str(i.price).replace(",",".")),2))
    return None

def isClient(nip,clients):
    if len(clients) == 0:
        return False
    for i in clients:
        if i.nip == nip:
            return True
    return False

def getID(nip, clients):
    for i in range(len(clients)):
        if clients[i].nip == nip:
            return i

def getSugarWeight(obj):
    return obj.sugarWeight

def ex1(transactions):
    clients = list()
    for i in transactions:
        if isClient(i.nip, clients) == True:
            clients[getID(i.nip, clients)].addSugar(int(i.weight))
        else:
            clients.append(Client(i.nip))
            clients[getID(i.nip, clients)].addSugar(int(i.weight))
    clients.sort(key=getSugarWeight, reverse=True)
    return [clients[0], clients[1], clients[2]]

# incorrect
def ex2(transactions,pricelist):
    cost = float(0)
    for i in transactions:
        cost += getCost(pricelist, i.date[0:4])
    return round(cost,2)


def ex3(transactions, pricelist):
    for i in transactions:
        year = i.date[0:4]
        for x in pricelist:
            if x.year == year:
                x.summaryWeight += int(i.weight)
                continue
    return pricelist

# incorrect
def ex4(transactions):
    discount = float(0.0)
    clients = list()
    for i in transactions:
        if isClient(i.nip, clients) == True:
            clients[getID(i.nip, clients)].addSugar(int(i.weight))
        else:
            clients.append(Client(i.nip))
            clients[getID(i.nip, clients)].addSugar(int(i.weight))
        iden = getID(i.nip, clients)
        w = clients[iden].sugarWeight
        if w >= 100 and w < 1000:
            discount += 5
        elif w >= 1000 and w < 10000:
            discount += 10
        elif w >= 10000:
            discount += 20
    return discount
    

def ex5(transactions,pricelist):
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

    ex_1 = ex1(transactions)
    ex_2 = ex2(transactions,pricelist)

    ex_3 = ex3(transactions,pricelist)
    ex_4 = ex4(transactions)
    print(ex_4)


if __name__ == "__main__":
    main()