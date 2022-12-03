package main

func intersection(a []int, b []int) []int {
  n := len(a)
  if len(b) > n {
    n = len(b)
  }
  r := make([]int, 0, n)
  var i, j int
  for i < len(a) && j < len(b) {
    if a[i] < b[j] {
      i++
    } else if a[i] > b[j] {
      j++
    } else {
      r = append(r, a[i])
      i++
      j++
    }
  }
  return r
}
