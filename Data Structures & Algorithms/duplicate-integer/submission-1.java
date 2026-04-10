class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int x: nums){
            count.put(x, count.getOrDefault(x, 0)+1);
            if(count.get(x)>1) return true;
        }
        return false;
    }
}
