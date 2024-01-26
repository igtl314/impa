def main():
    A, B = map(int, input().split())
    if 1 <= A <= 100000 and A <= B <= 100000:
        if A == 0 and B == 0:
            return
        count = 0
        for i in range(A, B + 1):
            if (i**0.5) % 1 == 0:
                count += 1
        print(count)


while True:
    try:
        main()
    except EOFError:
        break
