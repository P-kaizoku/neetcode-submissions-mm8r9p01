func hasDuplicate(nums []int) bool {
    mp := make(map[int]struct{})

	for _, i := range nums{
		if _, ok := mp[i]; ok{
			return true
		}
		mp[i] = struct{}{}
	}
	return false
}
