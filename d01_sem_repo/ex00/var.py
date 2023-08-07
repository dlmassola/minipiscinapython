def my_var():
    vInteiro = 42
    vString = "42"
    vString2 = "quarante-deux"
    vFloat = 42.0
    vBool = True
    vList = [42]
    vDict = {42: 42}
    vTuple = (42,)
    vSet = set()

    print(vInteiro, "has a type", type(vInteiro))
    print(vString, "has a type", type(vString))
    print(vString2, "has a type", type(vString2))
    print(vFloat, "has a type", type(vFloat))
    print(vBool ,"has a type", type(vBool))
    print(vList, "has a type", type(vList))
    print(vDict, "has a type", type(vDict))
    print(vTuple, "has a type", type(vTuple))
    print(vSet, "has a type", type(vSet))


if __name__ == '__main__':
    my_var()