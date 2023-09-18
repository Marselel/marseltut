package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scanln(&n)
	var values []int

	for i := 0; i < n; i++ {
		var val int
		fmt.Scanln(&val)
		// fmt.Println(fincBin(val))
		values = append(values, val)
	}
	for _, item := range values {

		fmt.Println(fincBin(item))

	}
}
func fincBin(val int) int {
	if val < 7 {
		return -1
	}
	binVal := fmt.Sprintf("%b", val)
	valList := strings.Split(binVal, "")
	counter := 0
	for i := 0; i < 3; i++ {

		if valList[i] == "1" {
			counter++
		} else {
			break
		}
	}

	return counter
}
func sliceToArray(ah []string) string {
	var b string
	for _, item := range ah {
		b += item
	}
	return b
}
func binToDesyat(val string) int64 {
	a := val
	b, _ := strconv.ParseInt(a, 2, 64)
	return b
}
