class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length = int(s[start:end])

            # we have found the word so the current index + 1
            start = end + 1
            end = start + length
            res.append(s[start:end])
            start = end
        return res
