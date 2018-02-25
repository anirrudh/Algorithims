//Go program to test out an implementation of insertion-sort.
package main

import (
	"fmt"
	"math/rand"
)

//A nice little function to fill the array
//The in-built function is deterministic, so it will produce
//The same numbers, unfortunately.
func arrayCreator(arr [10]int) [10]int {

	fmt.Println("emp:", arr)

	for i := 0; i < len(arr); i++ {
		f := rand.Intn(100)
		arr[i] = f
	}
	fmt.Println("filled:", arr)
	return arr
}

//A nice implementation of the C++ Version of this code :)
func insertionSort(arr [10]int) [10]int {
	for j := 1; j < len(arr); j++ {
		key := arr[j]
		i := j - 1
		for i >= 0 && arr[i] > key {
			arr[i+1] = arr[i]
			i = i - 1
		}
		arr[i+1] = key
	}
	fmt.Println("sorted:", arr)
	return arr
}

func main() {
	var arr [10]int
	arr = arrayCreator(arr)
	insertionSort(arr)
}
