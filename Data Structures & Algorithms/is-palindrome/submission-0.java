class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str = new StringBuilder("");
        
        for(char c: s.toCharArray()){
            if(Character.isLetterOrDigit(c)) str.append(c);
        }

        String original = str.toString().toLowerCase();
        String reversed = str.reverse().toString().toLowerCase();


        return original.equals(reversed);
    }
}
