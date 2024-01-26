import numpy as np


def take_over(new_owner, curr_owner, N):
    return (
        (new_owner == curr_owner - 1)
        or (new_owner == N - 1 and curr_owner == 0)
        or (new_owner == curr_owner)
    )


def main():
    line = input()
    if line == "0 0 0 0":
        exit()
    N, R, C, K = map(int, line.split())

    tree = np.zeros((R, C), dtype=int)

    for i in range(R):
        kingdom_row = list(map(int, input().split()))
        tree[i] = kingdom_row

    for i in range(K):
        new_tree = tree.copy()
        for r in range(R):
            for c in range(C):
                curr_owner = tree[r, c]
                neighbors = [
                    tree[max(0, r - 1), c],
                    tree[min(R - 1, r + 1), c],
                    tree[r, max(0, c - 1)],
                    tree[r, min(C - 1, c + 1)],
                ]

                for neighbor in neighbors:
                    if take_over(curr_owner, neighbor, N):
                        new_tree[r, c] = curr_owner

        tree = new_tree

    for r in range(R):
        for c in range(C):
            print(tree[r, c], end=" ")
        print()


while True:
    try:
        main()
    except EOFError:
        break
