package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func solve(filepath string) int {
	res := 0
	f, _ := os.Open(filepath)
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}

		big := math.MinInt64
		best := math.MinInt64
		for _, ch := range line {
			d := int(ch - '0')
			best = max(best, int(big*10+d))
			big = max(d, big)
		}

		res += best
	}
	return res
}

func solve2(filepath string) int {
	res := 0
	f, _ := os.Open(filepath)
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}

		rem := len(line) - 12
		stk := make([]byte, 0, len(line))
		for i := 0; i < len(line); i++ {
			for rem > 0 && len(stk) > 0 && stk[len(stk)-1] < line[i] {
				stk = stk[:len(stk)-1]
				rem--
			}
			stk = append(stk, line[i])
		}

		x, _ := strconv.Atoi(string(stk[:12]))
		res += x
	}
	return res
}

func main() {
	if solve("d3_test.in") != 357 {
		fmt.Println("failed p1 test")
	}
	if solve("d3.in") != 17535 {
		fmt.Println("failed p1")
	}
	if solve2("d3_test.in") != 3121910778619 {
		fmt.Println("failed p2 test")
	}
	if solve2("d3.in") != 173577199527257 {
		fmt.Println("failed p2")
	}
}
