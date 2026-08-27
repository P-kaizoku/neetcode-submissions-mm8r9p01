func isValid(s string) bool {
		  mp := map[byte]byte{
        '}': '{',
        ')': '(',
        ']': '[',
    }

			stack := make([]byte, 0, len(s))


			for i:=0; i<len(s); i++{
				c := s[i]
				if val, ok:=mp[c]; ok && len(stack) > 0 && stack[len(stack)-1] == byte(val){
					stack = stack[:len(stack)-1]
					continue
				}

				stack = append(stack, c)
			}

			return len(stack) == 0



}
