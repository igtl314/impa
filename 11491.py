import sys


def main():
    N, D = map(int, input().split())
    i = 0
    if N == 0 and D == 0:
        return
    s = input()
    stack = []
    for c in s:
        while D > 0 and stack and stack[-1] < c:
            stack.pop()
            D -= 1
            i += 1
        stack.append(c)
    if D > 0:
        stack = stack[:-D]
        i += D
    print("".join(stack[: (N - i)]))


# sys.stdout = open("output.txt", "w")
while True:
    try:
        main()
    except EOFError:
        break
# sys.stdout.close()
