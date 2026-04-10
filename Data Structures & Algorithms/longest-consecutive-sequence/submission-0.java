class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int longest = 0;

        for (int i: nums){
            set.add(i);
        }

        for(int num: set){
            if(!set.contains(num-1)){
                int length = 1;
                while(set.contains(num+length)) length++;
                longest = (longest>length)?longest:length;
            }


        }
        return longest;

    }
}
