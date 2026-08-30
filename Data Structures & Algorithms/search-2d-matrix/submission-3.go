func searchMatrix(matrix [][]int, target int) bool {
	m := len(matrix)
	n := len(matrix[0])

	t := m*n
	l, r := 0, t-1
	for l <= r{
		mid := r - (r-l)/2
		row := mid/n
		col := mid%n


		if matrix[row][col] == target{
			return true
		} else if matrix[row][col] > target{
			r = mid-1
		}else{
			l = mid+1
		}
	}
	return false
}
