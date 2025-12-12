from functools import cache
from collections import defaultdict, deque

def solve(input_file: str) -> int:
    g = defaultdict(list)

    with open(input_file, "r") as f:
        for line in f:
            ele = line.strip().split()
            g[ele[0][:-1]] = ele[1:]
    
    # dag wont inf loop
    res = 0
    q = deque(["you"])
    while q:
        curr = q.popleft()
        if curr == "out":
            res += 1
            continue

        for nxt in g[curr]:
            q.append(nxt)

    return res


def solve2(input_file: str) -> int:
    g = defaultdict(list)

    with open(input_file, "r") as f:
        for line in f:
            ele = line.strip().split()
            g[ele[0][:-1]] = ele[1:]
    
    @cache
    def dfs(curr, state):
        if curr == "out":
            return state == 3   # 0 - none, 1 - dac, 2 - fft, 3 - both

        if curr == "dac":
            state |= 1

        if curr == "fft":
            state |= 2

        res = 0
        for nxt in g[curr]:
            res += dfs(nxt, state)
        return res

    return dfs("svr", 0)

if __name__ == "__main__":
    assert solve("d11_test.in") == 5
    assert solve("d11.in") == 470

    assert solve2("d11_test_2.in") == 2
    assert solve2("d11.in") == 384151614084875
