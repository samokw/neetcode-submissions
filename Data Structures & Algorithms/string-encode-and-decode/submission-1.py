class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = 0
            while s[i] != "#": # We are grabbing the numbers infront of the delimiter
                length = length * 10 + int(s[i])
                i += 1
            i += 1 # Also skip the delimiter
            res.append(s[i: i + length])
            i += length
        return res