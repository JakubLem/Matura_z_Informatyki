

def ex1(rows):
    result = str("")
    for i in range(39,len(rows),40):
        result += rows[i][9]
    return result


def main():
    rows = open("Rozszerzona/maj2018/2czesc/Dane_PR2/sygnaly.txt", "r", encoding="utf-8").read().splitlines()
    ex_1 = ex1(rows)
    print(ex_1)


if __name__ == "__main__":
    main()