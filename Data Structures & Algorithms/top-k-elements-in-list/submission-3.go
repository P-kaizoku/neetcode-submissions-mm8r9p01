func topKFrequent(nums []int, k int) []int {
	mp := make(map[int]int)

	for _, n := range nums{
		mp[n]++
	}

	type Elem struct{
		k int
		v int
	}

	var arr []Elem

	for k,v := range mp{
		arr = append(arr, Elem{k, v})
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i].v > arr[j].v
	})

	res := []int{}

	for i:=0; i < k; i++{
		res = append(res, arr[i].k)
	}

	return res

}
