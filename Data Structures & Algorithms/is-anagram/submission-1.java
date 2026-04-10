class Solution {
    public boolean isAnagram(String s, String t) {
        
        int n = s.length(), m = t.length();

        if(n != m) return false;
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        for (int i=0; i<m; i++){
            char ele1 = s.charAt(i);
            char ele2 = t.charAt(i);
            map1.put(ele1, map1.getOrDefault(ele1, 0)+1);
            map2.put(ele2, map2.getOrDefault(ele2, 0)+1);
        }

        for (char key: map1.keySet()){
            if(!map2.containsKey(key) || !(map2.get(key).equals(map1.get(key)))) return false;
        }

        return true;


    }
}
