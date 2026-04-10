class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        for w in strs:
            len_w = str(len(w))
            encoded_w = len_w + "#" + w
            encoded_str += encoded_w
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_str = []

        i = 0
        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1
            
            len_w = int(s[i:j])

            w = s[j+1:j+1+len_w]
            decoded_str.append(w)
            i = j+1+len_w

        return decoded_str

