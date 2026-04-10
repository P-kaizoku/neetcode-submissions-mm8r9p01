class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if len(strs) == 0:
            return ""
        
        for word in strs:
            wordLength = str(len(word))
            encoded_str += wordLength + "#" + word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        if len(s)==0:
            return []
        
        j = 0
        for i in range(len(s)):
            if s[i]=="#" and s[i-1].isdigit():
                wordLength = int(s[j:i])
                word = s[i+1:wordLength+i+1]
                decoded_str.append(word)
                j = wordLength+i+1
        
        return decoded_str



