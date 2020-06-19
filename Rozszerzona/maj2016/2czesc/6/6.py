
def szyfruj(word,key):
    asciiArray = list()
    for i in word:
        asciiArray.append(ord(i))
    print("ascciArray:", asciiArray)
    siphrArray = list()
    for i in asciiArray:
        if int(int(i)+int(key)) > 90:
            siphrArray.append(int(i)-(90-int(i)+1))
        else:
            siphrArray.append(int(i)+int(key))
    """INCORRECT"""
    """INCORRECT"""

    """INCORRECT"""
    """INCORRECT"""
    """INCORRECT"""
    """INCORRECT"""
    """INCORRECT"""
    
    result = str("")
    for i in siphrArray:
        result += str(chr(i))
    return result

def ex_1():
    word_array = ["INTERPRETOWANIE"]
    key = 107
    result = list()
    for i in word_array:
        result.append(szyfruj(i,key))
    return result

def ex_2():
    pass

def ex_3():
    pass


def main():
    ex1 = ex_1()
    print(ex1)

if __name__ == "__main__":
    main()