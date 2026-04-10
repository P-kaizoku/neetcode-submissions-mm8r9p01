class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string ans = "";
        for (int i=0; i<n; i++){
            ans += to_string(strs[i].size()) + "#" + strs[i];
        }
        return ans;
    }

    string extractString(int i, int k, string s){
        string ans = "";
        
        for (int j=i; j<k; j++){
            ans += s[j];
        }

        return ans;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        string strLen = "";
        int len = 0;

        for (int i=0; i<s.size(); i++){
            if (s.at(i)=='#'){
                len = stoi(strLen);
                ans.push_back(extractString(i+1, i+1+len, s));
                strLen = "";
                i += len;
            }else{

            strLen += s[i];
            }
            
        }
        return ans;
    }
};
