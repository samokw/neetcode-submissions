class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, index = [], 0

        while index < len(s):
            delim = index
            while s[delim] != "#":
                delim += 1
            length = int(s[index:delim])
            res.append(s[delim + 1 : delim + 1 + length])
            index = delim + 1 + length
        return res
