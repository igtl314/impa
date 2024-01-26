import sys


def main():
    sys.stdout = open("output.txt", "w")
    case = 0
    while True:
        exit = False
        N, D = map(int, input().split())
        islands = []
        radars = []
        if N == 0 and D == 0:
            return
        case += 1
        for i in range(N):
            X, Y = map(int, input().split())
            if Y > D:
                exit = True
            islands.append((X, Y))
        islands.sort(key=lambda x: x[0])
        if exit:
            print("Case {}: -1".format(case))
            input()
            continue
        # Ser till att alla öar får en radar
        while len(islands) > 0:
            # Hämtar ön längst till vänster
            X, Y = islands.pop(0)
            # Räknar kordinat till vart radarn kan placerar längst till höger
            radar = X + (D**2 - Y**2)
            radars.append(radar)
            # Kollar vilka öar som ligger inom radarns räckvidd
            while len(islands) > 0:
                islandX, islandY = islands[0]
                distance = ((islandX - radar) ** 2 + islandY**2) ** 0.5
                if distance <= D:
                    islands.pop(0)
                else:
                    break
        print("Case {}: {}".format(case, len(radars)))
        input()


while True:
    try:
        main()
    except EOFError:
        break
