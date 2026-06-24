class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ''
        for word in strs:
            new_str += word + '\n'
        return new_str

    def decode(self, s: str) -> List[str]:
        new_list = []

        last_found = 0
        
        for i in range(len(s)):
            if s[i] == '\n':
                new_list.append(s[last_found:i])
                last_found = i+1
        return new_list