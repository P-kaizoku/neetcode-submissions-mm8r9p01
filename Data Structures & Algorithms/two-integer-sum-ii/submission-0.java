class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans[] = new int[2];
        for (int i=0; i<nums.length; i++){
            int diff = target - nums[i];
            if(map.containsKey(diff)){
                int j = map.get(diff);
                ans[0] = (i<j)?i+1:j+1;
                ans[1] = (i>j)?i+1:j+1;
                return ans;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
}
