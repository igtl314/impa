# N, R, C, K
# N number of heirs
# R and C dimensins of the kingdom
# K number of battles
# After that
# R lines with C ints
# original land distribution
# 0 0 0 0 is end of progrma

import copy


def take_over(new_owner, curr_owner, N):
    if new_owner == curr_owner - 1:
        return True
    elif new_owner == N - 1 and curr_owner == 0:
        return True
    elif new_owner == curr_owner:
        return True
    else:
        return False


def main():
    line = input()
    if line == "0 0 0 0":
        exit()
    N, R, C, K = map(int, line.split())
    tree = []
    for i in range(R):
        kingdom_row = input().split()
        row = []
        for j in range(C):
            row.append(int(kingdom_row[j]))
        tree.append(row)
    for i in range(K):
        new_tree = copy.deepcopy(tree)
        for r in range(R):
            if r == 0:
                for c in range(C):
                    curr_owner = tree[r][c]
                    if c == 0:
                        ##print("R=0 C=0")
                        right = tree[r][c + 1]
                        if take_over(curr_owner, right, N):
                            new_tree[r][c + 1] = curr_owner

                        down = tree[r + 1][c]
                        if take_over(curr_owner, down, N):
                            new_tree[r + 1][c] = curr_owner

                    else:
                        ##print("R,0 C !=0")
                        left = tree[r][c - 1]
                        if take_over(curr_owner, left, N):
                            new_tree[r][c - 1] = curr_owner

                        if c != C - 1:
                            right = tree[r][c + 1]
                            if take_over(curr_owner, right, N):
                                new_tree[r][c + 1] = curr_owner

                        down = tree[r + 1][c]
                        if take_over(curr_owner, down, N):
                            new_tree[r + 1][c] = curr_owner
            else:
                for c in range(C):
                    curr_owner = tree[r][c]
                    if c == 0:
                        # print("R!=0 C=0")
                        up = tree[r - 1][c]
                        if take_over(curr_owner, up, N):
                            new_tree[r - 1][c] = curr_owner
                        if r != R - 1:
                            down = tree[r + 1][c]
                            if take_over(curr_owner, down, N):
                                new_tree[r + 1][c] = curr_owner

                        right = tree[r][c + 1]
                        if take_over(curr_owner, right, N):
                            new_tree[r][c + 1] = curr_owner

                    else:
                        # print("R!=0 C!=0")
                        up = tree[r - 1][c]
                        if take_over(curr_owner, up, N):
                            new_tree[r - 1][c] = curr_owner

                        if r != R - 1:
                            down = tree[r + 1][c]
                            if take_over(curr_owner, down, N):
                                new_tree[r + 1][c] = curr_owner

                        left = tree[r][c - 1]
                        if take_over(curr_owner, left, N):
                            new_tree[r][c - 1] = curr_owner
                        if c != C - 1:
                            right = tree[r][c + 1]
                            if take_over(curr_owner, right, N):
                                new_tree[r][c + 1] = curr_owner

        tree = new_tree
    for r in range(R):
        for c in range(C):
            print(tree[r][c], end=" ")
        print()


while True:
    try:
        main()
    except EOFError:
        break
