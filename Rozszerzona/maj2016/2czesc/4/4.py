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
            self.onCirclePoinst = list()
            self.inCircle = 0

    answer = Answer()
    for i in points:
        if (pow(int(i[0])-int(200),2) + pow(int(i[1])-int(200),2) == pow(200,2)):
            answer.onCirclePoinst.append(i)
        elif pow(int(i[0])-int(200),2) + pow(int(i[1])-int(200),2) < pow(200,2):
            answer.inCircle += 1
    return answer


def main():
    data = open("Rozszerzona/maj2016/2czesc/Dane_PR2/punkty.txt", "r", encoding="utf-8").read().splitlines()
    points = toPointList(data)
    
    ex_1 = ex1(points)

    for i in ex_1.onCirclePoinst:
        print(i)
    print("--")
    print(ex_1.inCircle)




if __name__ == "__main__":
    main()