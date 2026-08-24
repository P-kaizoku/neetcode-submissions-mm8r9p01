type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	
	var builder strings.Builder
	builder.WriteString("")
	ans := builder.String()

	for _, word := range strs{
		x := len(word)
		ans += strconv.Itoa(x) + "#" + word
	}

	return ans


	
}

func (s *Solution) Decode(encoded string) []string {
	res := []string{}

	i := 0

	for i < len(encoded){
		j := i
		for encoded[j] != '#'{
			j++
		}
		strlen := encoded[i:j]
		low, _ := strconv.Atoi(strlen)
		i = j+1
		word := encoded[i:i+low]
		res = append(res, word)
		i += low
	}

	return res
}
