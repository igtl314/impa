import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, neighbor_dist in graph[curr_node]:
            dist = curr_dist + neighbor_dist
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances


def shortest_path(tree):
    cities = list(tree.keys())
    graph = {city: [] for city in cities}
    for city, neighbors in tree.items():
        for neighbor, cost in neighbors:
            graph[city].append((neighbor, cost))
            graph[neighbor].append((city, cost))
    min_cost = float("inf")
    for city in cities:
        distances = dijkstra(graph, city)
        total_cost = sum(distances.values())
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = list(distances.keys())
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
        bestpath, min_cost = shortest_path(tree)
        print(min_cost)


while True:
    try:
        main()
    except EOFError:
        break
