def main():
    n = int(input())
    for i in range(n):
        a = map(int, input().split())
        a = sorted(a)
        print("Case %d: %d" % (i + 1, a[1]))


while True:
    try:
        main()
    except EOFError:
        break
