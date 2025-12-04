def solve(input_file: str) -> int:
    ranges = []
    with open(input_file, "r") as f:
        for line in f:
            for r in line.strip().split(","):
                t = r.split("-")
                if len(t) != 1:
                    ranges.append(t)

    res = 0
    for ran in ranges:
        a_str, a, b_str, b = ran[0], int(ran[0]), ran[1], int(ran[1])
        smallest = (len(a_str) // 2)
        largest = (len(b_str) // 2)

        for k in range(smallest, largest + 1):
            for i in range(1, 10**k):
                cand = int(str(i) + str(i))
                if a <= cand <= b:
                    res += cand

    return res


def solve2(input_file: str) -> int:
    ranges = []
    with open(input_file, "r") as f:
        for line in f:
            for r in line.strip().split(","):
                t = r.split("-")
                if len(t) != 1:
                    ranges.append(t)

    res = 0
    seen = set()
    for ran in ranges:
        a_str, a, b_str, b = ran[0], int(ran[0]), ran[1], int(ran[1])

        for length in range(len(a_str), len(b_str) + 1):
            for pat_length in range(1, length // 2 + 1):
                if length % pat_length != 0:
                    continue
                reps = length // pat_length

                for i in range(10**(pat_length-1), 10**pat_length):
                    cand = int(str(i) * reps)
                    if a <= cand <= b:
                        if cand not in seen:
                            res += cand
                            seen.add(cand)

    return res


if __name__ == "__main__":
    assert solve("d2_test.in") == 1227775554
    assert solve("d2.in") == 18952700150

    assert solve2("d2_test.in") == 4174379265
    assert solve2("d2.in") == 4174379265
