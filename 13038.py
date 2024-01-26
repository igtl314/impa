def deepFirst(tree, start, sets):
    visited = []
    toTraverse = [start]
    while len(toTraverse) > 0:
        current = toTraverse.pop()
        if current not in visited:
            visited.append(current)
            if current in tree:
                for child in tree[current]:
                    appendBool = True
                    for s in sets:
                        if child in s:
                            appendBool = False
                    if appendBool:
                        toTraverse.append(child)
    return visited


# om den inte finns sätt bool till true och lägg till i sets


def main():
    n = int(input())
    answer = []
    input()
    for i in range(n):
        loop = True
        tree = {}
        sets = []
        while loop:
            a = input()
            if a == "":
                loop = False
                break
            u, v = map(int, a.split())
            if u not in tree:
                tree[u] = []
            tree[u].append(v)
        for node in tree:
            appendBool = True
            for s in sets:
                if node in s:
                    appendBool = False
            if appendBool:
                sets.append(deepFirst(tree, node, sets))
        answer.append(len(sets))
    for i in range(n):
        print(f"Case {i+1}: {answer[i]}")


while True:
    try:
        main()
    except EOFError:
        break
