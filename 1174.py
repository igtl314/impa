# from itertools import permutations


def total_cost(path, tree):
    cost = 0
    for i in range(len(path) - 1):
        city1, city2 = path[i], path[i + 1]
        for neighbor, neighbor_cost in tree[city1]:
            if neighbor == city2:
                cost += neighbor_cost
                break
    return cost


def dfs(city, visited, tree, path, cost, best_path, min_cost):
    visited.add(city)
    path.append(city)
    if len(path) == len(tree):
        if cost < min_cost:
            min_cost = cost
            best_path[:] = path
    else:
        for neighbor, neighbor_cost in tree[city]:
            if neighbor not in visited:
                min_cost = dfs(
                    neighbor,
                    visited,
                    tree,
                    path,
                    cost + neighbor_cost,
                    best_path,
                    min_cost,
                )
    visited.remove(city)
    path.pop()
    return min_cost


def shortest_path(tree):
    cities = list(tree.keys())
    best_path = []
    min_cost = float("inf")
    for city in cities:
        temp_min_cost = dfs(city, set(), tree, [], 0, best_path, min_cost)
        if temp_min_cost < min_cost:
            min_cost = temp_min_cost
    return best_path, min_cost


def main():
    i = int(input())
    for x in range(i):
        tree = {}
        input()
        m = int(input())  # Number of cities
        n = int(input())  # Number of links
        for i in range(n):
            city1, city2, cost = input().split()
            cost = int(cost)
            if city1 not in tree:
                tree[city1] = []
            if city2 not in tree:
                tree[city2] = []
            tree[city1].append((city2, cost))
            tree[city2].append((city1, cost))
            cities = list(tree.keys())
        bestpath, min_cost = shortest_path(tree)
        print(f"Total Cost: {min_cost}")
        print(f"Cheapest Path: {bestpath}")

        # Initialize variables to store the best path and its cost
        # best_path = None
        # min_cost = float("inf")

        # # Generate all possible permutations of cities
        # for perm in permutations(cities):
        #     cost = total_cost(perm, tree)
        #     if cost < min_cost:
        #         min_cost = cost
        #         best_path = perm
        # # Initialize variables to store the best path and its cost
        # best_path = None
        # min_cost = float("inf")

        # # Generate all possible permutations of cities
        # for perm in permutations(cities):
        #     cost = total_cost(perm, tree)
        #     if cost < min_cost:
        #         min_cost = cost
        #         best_path = perm
        # print(f"Total Cost: {min_cost}")
        # print(f"Cheapest Path: {best_path}")


while True:
    try:
        main()
    except EOFError:
        break
