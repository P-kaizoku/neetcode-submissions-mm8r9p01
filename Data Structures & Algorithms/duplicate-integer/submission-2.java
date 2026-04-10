class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int x: nums){
           if(count.containsKey(x)) return true;
           count.put(x, 1);
        }
        return false;
    }
}
