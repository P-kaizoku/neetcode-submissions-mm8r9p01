func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)

	for i, v := range nums {
		diff := target - nums[i]

		if _, ok := mp[diff]; ok {
			return []int{mp[diff], i}
		}

		mp[v] = i
	}
	return []int{}
}
