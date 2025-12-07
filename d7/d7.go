package main

import (
	"bufio"
	"fmt"
	"os"
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

	prev := make([]int, cols)
	for i := 0; i < cols; i++ {
		if lines[0][i] == 'S' {
			prev[i] = 1
		} else {
			prev[i] = 0
		}
	}

	for i := 1; i < rows; i++ {
		curr := make([]int, cols)
		for j := 0; j < cols; j++ {
			curr[j] = 0
		}

		for j := 0; j < cols; j++ {
			if lines[i][j] == '^' {
				if j+1 < len(lines[j]) {
					curr[j+1] += prev[j]
				}
				if j-1 >= 0 {
					curr[j-1] += prev[j]
				}
			} else if prev[j] > 0 {
				curr[j] += prev[j]
			}
		}

		prev = curr
	}

	res := 0
	for i := 0; i < cols; i++ {
		res += prev[i]
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
	if solve2("d7_test.in") != 40 {
		fmt.Println("failed p2 test")
	}
	if solve2("d7.in") != 29893386035180 {
		fmt.Println("failed p2")
	}
}
