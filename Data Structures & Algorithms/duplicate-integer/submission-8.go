func hasDuplicate(nums []int) bool {
    mp := make(map[int]bool)

    for _, num := range nums{
        if _,exists := mp[num]; exists{
            return true
        }
        mp[num] = true
    }
    return false
}
