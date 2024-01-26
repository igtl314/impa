def getPrefixes(str: str):
    if str == "m":
        return 0.001
    elif str == "k":
        return 1000
    elif str == "M":
        return 1000000


def getFunction(temp: dict):
    if "P" in temp and "U" in temp:
        return "I=" + "{:.2f}".format(round(temp["P"] / temp["U"], 2)) + "A"
    elif "P" in temp and "I" in temp:
        return "U=" + "{:.2f}".format(round(temp["P"] / temp["I"], 2)) + "V"
    elif "U" in temp and "I" in temp:
        return "P=" + "{:.2f}".format(round(temp["U"] * temp["I"], 2)) + "W"
    else:
        return -1


def main():
    n = int(input())
    prefixes = ["m", "k", "M"]
    units = ["W", "A", "V"]
    Concepts = ["P", "U", "I"]
    for i in range(n):
        temp = {}
        lineArr = input().replace(",", "").split()
        for line in lineArr:
            if line[-1] == ".":
                line = line[:-1]
            if line[-1] in units and line[0] in Concepts:
                if line[-2] in prefixes:
                    temp[line[0]] = float(line[2:-2]) * getPrefixes(line[-2])
                else:
                    temp[line[0]] = float(line[2:-1])

        print("Problem #%d" % (i + 1))
        print(getFunction(temp))
        print()


while True:
    try:
        main()
    except EOFError:
        break
