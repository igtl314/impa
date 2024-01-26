def main():
    try:
        v, t = map(int, input().split())
    except ValueError:
        exit()
    print(v * t * 2)


while True:
    try:
        main()
    except EOFError:
        break
