import math

# funkcja ma zwracać ze stringa '22 22' listę [22,22] --> czyli listę list w przypadku wielu obiektów
def toPointList(data):
    result = list()
    for i in data:
        result.append(i.split())
    return result


def ex1(points):
    class Answer:
        def __init__(self):
            self.points = list()
            self.onCircle = 0
    answer = Answer()
    


def main():
    data = open("Rozszerzona/maj2016/2czesc/Dane_PR2/punkty.txt", "r", encoding="utf-8").read().splitlines()
    points = toPointList(data)
    
    ex_1 = ex1(points)





if __name__ == "__main__":
    main()