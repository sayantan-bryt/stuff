// _Functions_ are central in Go. We'll learn about
// functions with a few different examples.

package main

import (
	"fmt"
)

func plus(a int, b int) int {
	return a + b
}

// has access to fields but not attributes
type TNumber int

func (x TNumber) toInt() (int) {
  return int(x)
}

func (x TNumber) mul(a int, b int) (int) {
	return  x.toInt() * (a + b)
}

// has access to both fields and attributes
type SNumber struct {
  *int
}

func (xs SNumber) mul(a int) (int) {
  return *(xs.int) * a
}

func (xs SNumber) toInt() (int) {
  return *(xs.int)
}


func summer[K comparable, V int64 | float64](m map[K]V) V {
  var s V
  for _, ele := range m {
    s += ele
  }
  return s
}


type Number interface {
  int64 | float64
}

func summerInterface[K comparable, V Number](m map[K]V) V {
  var s V
  for _, ele := range m {
    s += ele
  }
  return s
}

func main() {
  a, b := 1, 2
	res := plus(a, b)
	fmt.Println(a, "+", b,"=", res)

  const number TNumber = 999
  numberMul := number.mul(a, b)
  fmt.Println(number, "* (", a, "+", b, ") =", numberMul)


  x := 999
  sNumber := SNumber{&x}
  sNumberMul := sNumber.mul(b)
  fmt.Println(sNumber.toInt(), "*", b , "=", sNumberMul)

  // spread operator; more like [:] in python
  stooges := [...]string{"hey", "there", "Delilah"}
  fmt.Println(stooges)
  copyStooges := stooges[:]
  fmt.Println(copyStooges)


  // templated function
  // Initialize a map for the integer values
  ints := map[string]int64{
    "first":  34,
    "second": 12,
  }

  // Initialize a map for the float values
  floats := map[string]float64{
    "first":  35.98,
    "second": 26.99,
  }

  fmt.Println("Summing floats and ints", summer(ints), summer(floats))
  fmt.Println("Summing floats and ints", summerInterface(ints), summerInterface(floats))

}
