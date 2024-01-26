bigArr = []
for i in range(32):
    for j in range(32):
        bigArr.append(2**i * 3**j)
bigArr.sort()

while True:
    try:
        m = int(input())
    except ValueError:
        break
    if m == 0:
        break
    for i in range(len(bigArr)):
        if bigArr[i] >= m:
            print(bigArr[i])
            break
