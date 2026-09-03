class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = dict()
        arr=[]
        for elem in strs:
            if "".join(sorted(elem)) not in seen:
                seen["".join(sorted(elem))] = [elem]
            else:
                seen["".join(sorted(elem))] = seen["".join(sorted(elem))] + [elem]

        return [elem for elem in seen.values()]