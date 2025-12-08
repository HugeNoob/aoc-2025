import math

def solve(input_file: str) -> int:
    boxes = []
    with open(input_file, "r") as f:
        for line in f:
            boxes.append(list(map(int, line.strip().split(","))))
    
    n = len(boxes)
    dists = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2)
            dists.append([dist, i, j])

    dists.sort()
    
    par = [i for i in range(n)]
    weight = [1] * n

    def union(a, b):
        p1, p2 = find(a), find(b)

        if p1 == p2:
            return False
        elif weight[p1] < weight[p2]:
            par[p1] = p2
            weight[p2] += weight[p1]
        else:
            par[p2] = p1
            weight[p1] += weight[p2]
        return True

    def find(x):
        while x != par[x]:
            par[x] = par[par[x]]
            x = par[x]
        return x

    iters = 10 if input_file == "d8_test.in" else 1000
    for i in range(min(n, iters)):
        union(dists[i][1], dists[i][2])

    par_weights = sorted([(w, p) for w, p in zip(weight, par)], reverse=True)

    res = 1
    for i in range(3):
        res *= par_weights[i][0]
    return res

def solve2(input_file: str) -> int:
    boxes = []
    with open(input_file, "r") as f:
        for line in f:
            boxes.append(list(map(int, line.strip().split(","))))
    
    n = len(boxes)
    dists = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2)
            dists.append([dist, i, j])

    dists.sort()
    
    par = [i for i in range(n)]
    weight = [1] * n

    def union(a, b):
        p1, p2 = find(a), find(b)

        if p1 == p2:
            return -1
        elif weight[p1] < weight[p2]:
            par[p1] = p2
            weight[p2] += weight[p1]
        else:
            par[p2] = p1
            weight[p1] += weight[p2]
        return max(weight[p1], weight[p2])

    def find(x):
        while x != par[x]:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for w, a, b in dists:
        w = union(a, b)
        if w == n:
            return boxes[a][0] * boxes[b][0]
    
    return -1

if __name__ == "__main__":
    assert solve("d8_test.in") == 40
    assert solve("d8.in") == 105952

    assert solve2("d8_test.in") == 25272
    assert solve2("d8.in") == 975931446
