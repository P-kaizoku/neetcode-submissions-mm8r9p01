class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ans[] = new int[2];
        for (int i=0; i<nums.length; i++){
            for(int j=0; j<nums.length; j++){
                if(i!=j && target == nums[i]+nums[j]) {
                    ans[0] = (i>j)?j:i;
                    ans[1] = (i>j)?i:j;
                } 
            }
        }
        return ans;
    }
}
