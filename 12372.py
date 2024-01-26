def main():
    try:
        n = int(input())
    except ValueError:
        return
    for i in range(n):
        try:
            l, w, h = map(int, input().split())
        except ValueError:
            return
        if l > 20 or w > 20 or h > 20:
            print("Case {}: bad".format(i + 1))
        else:
            print("Case {}: good".format(i + 1))


while True:
    try:
        main()
    except EOFError:
        break
