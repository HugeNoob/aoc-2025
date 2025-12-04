def solve(input_file: str) -> int:
    lines = []
    with open(input_file, "r") as f:
        for line in f:
            lines.append(line.strip())
    
    res = 0
    rows, cols = len(lines), len(lines[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != '@':
                continue

            papers = 0
            for rm, cm in dirs:
                nr, nc = r + rm, c + cm
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                papers += lines[nr][nc] == '@'
            res += papers < 4

    return res        


def solve2(input_file: str) -> int:
    lines = []
    with open(input_file, "r") as f:
        for line in f:
            lines.append(list(line.strip()))
    
    res = 0
    rows, cols = len(lines), len(lines[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rem = True

    while rem:
        rem = False

        to_rem = []
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] != '@':
                    continue

                papers = 0
                for rm, cm in dirs:
                    nr, nc = r + rm, c + cm
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    papers += lines[nr][nc] == '@'

                if papers < 4:
                    res += 1
                    to_rem.append([r, c])
                    rem = True
        
        for r, c in to_rem:
            lines[r][c] = '.'

    return res        

if __name__ == "__main__":
    assert solve("d4_test.in") == 13
    assert solve("d4.in") == 1549

    assert solve2("d4_test.in") == 43
    assert solve2("d4.in") == 8887
