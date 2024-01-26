def deepFirst(tree, start, sets, memo):
    visited = set()
    toTraverse = [start]
    while toTraverse:
        current = toTraverse.pop()
        if current not in visited:
            visited.add(current)
            if current in tree:
                for child in tree[current]:
                    if not any(child in s for s in sets):
                        toTraverse.append(child)
    memo[start] = visited
    return visited


def main():
    n = int(input())
    answer = []
    input()
    for i in range(n):
        tree = {}
        memo = {}
        sets = []
        while True:
            a = input()
            if not a:
                break
            u, v = map(int, a.split())
            tree.setdefault(u, []).append(v)
        for node in tree:
            if node in memo:
                visited = memo[node]
            else:
                visited = deepFirst(tree, node, sets, memo)
            if not any(node in s for s in sets):
                sets.append(visited)
                for s in sets[:-1]:
                    if node in s:
                        sets.remove(s)
                        visited = visited.union(s)
                        memo.update({n: visited for n in s})
                        break
        answer.append(len(sets))
    for i, ans in enumerate(answer, 1):
        print(f"Case {i}: {ans}")


while True:
    try:
        main()
    except EOFError:
        break
