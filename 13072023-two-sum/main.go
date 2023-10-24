package main

import "fmt"

func twoSum(nums []int, target int) []int {

	hashMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		complement := target - nums[i]
		if v, ok := hashMap[complement]; ok {
			return []int{v, i}
		}
		hashMap[complement] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{3, 3}, 6))
}
