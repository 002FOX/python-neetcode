def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for string in strs:
                if len(string) == i or strs[0][i] != string[i]:
                    return prefix
            prefix += string[i]
        return prefix