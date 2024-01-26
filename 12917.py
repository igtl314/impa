def main():
    P, H, O = map(int, input().split())
    if 1 <= P <= 5 and 1 <= H <= 5 and 1 <= P <= O <= 10:
        if (O - P) < H:
            print("Hunters win!")
        else:
            print("Props win!")


while True:
    try:
        main()
    except EOFError:
        break
