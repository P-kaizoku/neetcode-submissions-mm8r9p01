class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>(3);
        Stack<Character> stack = new Stack<>();

        map.put('[',']');
        map.put('{', '}');
        map.put('(',')');

        for (char c: s.toCharArray()){
            if(c == '[' || c == '{' || c == '('){
                stack.push(c);
            }else{
                if(stack.isEmpty()) return false;

                if(map.get(stack.pop()) != c) return false;
            }
        }
        return stack.isEmpty();
    }
}
