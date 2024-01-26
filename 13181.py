import math


def main():
    testcases = input()
    furthest = 0
    temp = 0
    firstbed = False
    for bed in range(len(testcases)):
        if testcases[bed] == "X":
            if firstbed == False:
                if temp > furthest:
                    furthest = temp - 1
                firstbed = True
            else:
                if temp > furthest:
                    furthest = math.floor(temp / 2)
            temp = 0
        elif testcases[bed] == ".":
            temp += 1
    print(furthest)


while True:
    try:
        main()
    except EOFError:
        break
