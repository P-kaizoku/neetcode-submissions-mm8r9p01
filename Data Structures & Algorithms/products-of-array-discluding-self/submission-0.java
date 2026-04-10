class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int arr[] = new int[n];

        arr[0] = 1;
        for(int i=1; i<n; i++){
            //storing the cummulative left product in the array.
            arr[i] = arr[i-1]*nums[i-1];
            
        }

        int cummRP = 1;
        for (int i=n-1; i>=0; i--){
            //storing the cumm right prod
            arr[i] *= cummRP;
            // calculating the cumm right prod.
            cummRP *= nums[i];
        }

        return arr;
    }
}  
