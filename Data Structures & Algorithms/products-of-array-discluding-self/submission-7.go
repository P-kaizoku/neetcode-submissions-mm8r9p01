func productExceptSelf(nums []int) []int {
	n := len(nums)

	leftArr := make([]int, n)

	leftArr[0]=1
	for i:=1; i<n; i++{
		leftArr[i] = leftArr[i-1]*nums[i-1]
	}

	r := 1

	for i:=n-2; i>=0; i--{
		r *= nums[i+1]
		leftArr[i] *= r
	}

	return leftArr



}
