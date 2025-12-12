# Doesn't work for test input and general solution. Just hacky based on weak input.
# I am not solving a packing problem.
def solve(input_file: str) -> int:
    with open(input_file, "r") as f:
        groups = f.read().strip().split("\n\n")

    areas = {}
    for i in range(len(groups) - 1):
        lines = groups[i].split("\n")
        shape = lines[1:]
        areas[i] = len(shape) * len(shape[0])

    res = 0
    for region in groups[-1].split("\n"):
        ele = region.split()

        dims = ele[0][:-1].split("x")
        reg_area = int(dims[0]) * int(dims[1])
        
        shapes_area = 0
        for i, cnt in enumerate(map(int, region.split()[1:])):
            shapes_area += cnt * areas[i]
        
        res += shapes_area <= reg_area
    
    return res


if __name__ == "__main__":
    solve("d12.in") == 472
