func isValidSudoku(board [][]byte) bool {

	for i := range 9{
	row := make(map[byte]struct{})
	col := make(map[byte]struct{})
		for j := range 9{
			er := board[i][j]
			if er != '.'{

			if _, ok := row[er]; ok{
				return false
			}
			row[er] = struct{}{}
			}

			ec := board[j][i]
			if ec != '.'{

			if _, ok := col[ec]; ok{
				return false
			}
			col[ec] = struct{}{}
			}
		}
	}


	for r:=0; r<9; r+=3{
		for c:=0; c<9; c+=3{

			seen := make(map[byte]struct{})

			for i := range 3{
				for j := range 3{
					e := board[i+r][j+c]
					if e != '.'{
						if _, ok := seen[e]; ok{
							return false
						}
						seen[e] = struct{}{}
					}
				}
			}
		}
	}
	
	return true

	
}
