func groupAnagrams(strs []string) [][]string {
	mp := make(map[string][]string)

	for _, s := range strs{
		chars := []byte(s)
		sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j]})
		x := string(chars)

		
		mp[x] = append(mp[x], s)
	}

	res := [][]string{}

	for _, v := range mp{
		res = append(res, v)
	}

	return res
}
