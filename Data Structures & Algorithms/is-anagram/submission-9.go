func isAnagram(s string, t string) bool {
	mp1 := make(map[rune]int)

	for _, c := range s{
		mp1[c]++
	}

	for _, c := range t{
		mp1[c]--
	}

	for _, v := range mp1{
		if v != 0{
			return false
		}
	}

	return true
}
