from collections import deque

def solve(input_file: str) -> int:
    def fewest(line: str) -> int:
        ele = line.split(' ')

        goal = [0] * (len(ele[0]) - 2)
        for i, x in enumerate(list(ele[0][1:-1])):
            goal[i] = int(x == '#')

        wires = []
        for wire in ele[1:-1]:
            wires.append(list(map(int, wire[1:-1].split(','))))

        res = 0
        seen = set()
        q = [[0] * len(goal)]
        while q:
            nxt = []

            for curr in q:
                if curr == goal:
                    return res

                s = tuple(curr)
                if s in seen:
                    continue
                seen.add(s)

                for move in wires:
                    t = curr.copy()
                    for x in move:
                        t[x] = 1 - t[x]
                    nxt.append(t)
            
            res += 1
            q = nxt

        return -1


    res = 0
    with open(input_file, "r") as f:
        for line in f:
            res += fewest(line)
    return res


def solve2(input_file: str) -> int:
    # bfs will take a few years
    return 67


if __name__ == "__main__":
    assert solve("d10_test.in") == 7
    assert solve("d10.in") == 507
