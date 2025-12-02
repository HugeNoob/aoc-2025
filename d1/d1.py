def solve(input_file: str) -> int:
    res = 0
    curr = 50

    with open(input_file, "r") as f:
        for rot in f:
            rot = rot.strip() 

            num = int(rot[1:])
            if rot[0] == "L":
                curr = (curr - num) % 100
            else:
                curr = (curr + num) % 100

            res += curr == 0
    
    return res


def solve2(input_file: str) -> int:
    res = 0
    curr = 50

    with open(input_file, "r") as f:
        for rot in f:
            rot = rot.strip() 

            num = int(rot[1:])
            res += num // 100

            if rot[0] == "L":
                if num % 100 >= curr and curr != 0:
                    res += 1
                curr = (curr - num) % 100
            else:
                if num % 100 >= 100 - curr and curr != 0:
                    res += 1
                curr = (curr + num) % 100
    
    return res


if __name__ == "__main__":
    assert solve("d1_test.in") == 3
    assert solve("d1.in") == 1040

    assert solve2("d1_test.in") == 6
    assert solve2("d1.in") == 6027
