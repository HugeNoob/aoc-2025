from itertools import zip_longest


def solve(input_file: str) -> int:
    qns = []
    with open(input_file, "r") as f:
        for line in f:
            qns.append(list(filter(lambda x: x != "", line.strip().split(" "))))
    
    res = 0
    for col in range(len(qns[0])):
        if qns[-1][col] == "+":
            add = True
            curr = 0
        else:
            add = False
            curr = 1

        for row in range(len(qns) - 1):
            if add:
                curr += int(qns[row][col])
            else:
                curr *= int(qns[row][col])
        
        res += curr

    return res        


def solve2(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    columns = list(zip_longest(*lines, fillvalue=' '))
    qns = []
    curr_nums = []
    curr_op = None

    for col in columns:
        if all(c == ' ' for c in col):
            if curr_nums:
                qns.append((curr_nums[::-1], curr_op))
                curr_nums = []
                curr_op = None
        else:
            num_str = ''.join(col[:-1]).strip()
            if num_str:
                curr_nums.append(int(num_str))
            if col[-1] != " ":
                curr_op = col[-1]
    
    if curr_nums:
        qns.append((curr_nums[::-1], curr_op))
    
    res = 0
    for qn, op in qns:
        if op == "+":
            add = True
            curr = 0
        else:
            add = False
            curr = 1

        for num in qn:
            if add:
                curr += int(num)
            else:
                curr *= int(num)
        
        res += curr
    
    return res
    

if __name__ == "__main__":
    assert solve("d6_test.in") == 4277556
    assert solve("d6.in") == 6725216329103

    assert solve2("d6_test.in") == 3263827
    assert solve2("d6.in") == 10600728112865
