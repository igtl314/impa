def main():
    try:
        n = int(input())
    except ValueError:
        return
    if n == 0:
        quit()
    if n == 1:
        return
    # for i in range(n + 1):
    try:
        case = list(map(int, input().split()))

    except ValueError:
        return
    testcase = []
    for i in range(n):
        testcase.append(case[i])
    testcase = sorted(testcase)
    cost = 0

    while len(testcase) > 1:
        a = testcase.pop(0)
        b = testcase.pop(0)
        testcase.append(a + b)
        cost += a + b
        testcase = sorted(testcase)
    print(cost)


while True:
    try:
        main()
    except EOFError:
        break
