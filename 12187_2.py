def perform_battles(N, R, C, K, land):
    for _ in range(K):
        new_land = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                adjacent_counts = [0] * N
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        adjacent_counts[land[nr][nc]] += 1
                for i in range(N):
                    if (i + 1) % N == land[r][c]:
                        new_land[r][c] = (land[r][c] + 1) % N
                    elif adjacent_counts[i] > 0:
                        new_land[r][c] = i
        land = new_land
    return land


while True:
    N, R, C, K = map(int, input().split())
    if N == 0:
        break

    land = [list(map(int, input().split())) for _ in range(R)]

    result = perform_battles(N, R, C, K, land)

    for row in result:
        print(" ".join(map(str, row)))
