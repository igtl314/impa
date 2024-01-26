def main():
    try:
        testcases = int(input())
    except ValueError:
        return
    for i in range(testcases):
        try:
            numberOfWalls = int(input())
        except ValueError:
            return
        walls = map(int, input().split())
        highJumps = 0
        lowJumps = 0
        prev = next(walls)
        for wall in walls:
            if wall > prev:
                highJumps += 1
            elif wall < prev:
                lowJumps += 1
            prev = wall
        print("Case {}: {} {}".format(i + 1, highJumps, lowJumps))


while True:
    try:
        main()
    except EOFError:
        break
