package main

import "fmt"

func gcd(a int, b int) int {
	if a%b == 0 {
		return b
	}
	return gcd(b, a%b)
}

func solution(w int, h int) int64 {
	var gcdv = gcd(w, h)
	w, h = w/gcdv, h/gcdv
	var eachb = 0
	if w == 1 {
		eachb = h
	} else {
		for x := 0; x < w; x++ {
			cy := h * x / w
			ny := (h*(x+1) + w - 1) / w
			eachb += ny - cy
		}
	}
	return int64(w*gcdv)*int64(h*gcdv) - int64(eachb)*int64(gcdv)
}
func main() {
	fmt.Println(solution(8, 12))
}
