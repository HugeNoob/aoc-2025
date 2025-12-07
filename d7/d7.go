package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solve(filepath string) int {
	lines := []string{}
	f, _ := os.Open(filepath)
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}
		lines = append(lines, line)
	}

	rows := len(lines)
	cols := len(lines[0])
	res := 0
	prev := []rune(lines[0])

	for i := 1; i < rows; i++ {
		curr := make([]rune, cols)
		for j := 0; j < cols; j++ {
			curr[j] = '.'
		}

		for j := 0; j < cols; j++ {
			add := false

			if lines[i][j] == '^' {
				if prev[j] == 'S' && j+1 < len(lines[j]) {
					curr[j+1] = 'S'
					add = true
				}
				if prev[j] == 'S' && j-1 >= 0 {
					curr[j-1] = 'S'
					add = true
				}
				curr[j] = '^'

				if add {
					res++
				}
			} else if prev[j] == 'S' {
				curr[j] = 'S'
			}
		}

		prev = curr
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
	if solve("d7_test.in") != 21 {
		fmt.Println("failed p1 test")
	}
	if solve("d7.in") != 1605 {
		fmt.Println("failed p1")
	}
	// if solve2("d7_test.in") != 3121910778619 {
	// 	fmt.Println("failed p2 test")
	// }
	// if solve2("d7.in") != 173577199527257 {
	// 	fmt.Println("failed p2")
	// }
}
