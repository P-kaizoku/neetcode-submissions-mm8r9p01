class Solution {

    public String encode(List<String> strs) {
        StringBuilder st = new StringBuilder();

        for (String str: strs){
            st.append(str.length()).append("#").append(str);
        }

        return st.toString();
    }

    public List<String> decode(String str) {
        List<String> ans  = new ArrayList<>();

        int i = 0;
        while(i<str.length()){

            int j = str.indexOf("#", i);
            int length = Integer.parseInt(str.substring(i, j));
            i = j+1;
            ans.add(str.substring(i, i+length));
            i+=length;

        }
        return ans;
    }
}
