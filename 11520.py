def main():
    try:
        testcases = int(input())
    except ValueError:
        exit()
    for i in range(testcases):
        try:
            dimmension = int(input())
        except ValueError:
            exit()
        if dimmension < 1 or dimmension > 10:
            exit()
        grid = []
        for j in range(dimmension):
            grid.append(list(input()))
        for j in range(dimmension):
            for k in range(dimmension):
                if grid[j][k] == ".":
                    for l in range(65, 91):
                        if (
                            not (j > 0 and grid[j - 1][k] == chr(l))
                            and not (j < dimmension - 1 and grid[j + 1][k] == chr(l))
                            and not (k > 0 and grid[j][k - 1] == chr(l))
                            and not (k < dimmension - 1 and grid[j][k + 1] == chr(l))
                        ):
                            grid[j][k] = chr(l)
                            break
        print("Case " + str(i + 1) + ":")
        for j in range(dimmension):
            print("".join(grid[j]))


while True:
    try:
        main()
    except EOFError:
        break
