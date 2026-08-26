func longestConsecutive(nums []int) int {
	set := make(map[int]struct{})

	for _, num := range nums{
		set[num] = struct{}{}
	}

	lcs := 0

	for _, num := range nums{
		if _, ok := set[num-1]; ok{
			continue
		}
		start := num
		currL := 1
		for {
			if _, ok:=set[start+1]; !ok{
				break
			}
			currL++
			start++
		}
		if currL > lcs{
			lcs = currL
		}
	}
	return lcs

}
