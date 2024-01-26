def main():
    case = 0
    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            return
        else:
            case += 1
        numbers = []
        guesses = []
        for _ in range(N):
            numbers.append(int(input()))
        numbers.sort()
        for _ in range(Q):
            guesses.append(int(input()))
        print("CASE# {}: ".format(case))
        for guess in guesses:
            if guess in numbers:
                print("{} found at {}".format(guess, numbers.index(guess) + 1))
            else:
                print("{} not found".format(guess))


while True:
    try:
        main()
    except EOFError:
        break
