class Solution:
    """
    一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。
    """
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        # 考虑第二个字母
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            # 当出现连续两个0
            if s[i - 1] + s[i] == "00": return 0
            # 考虑单个字母
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # 考虑两个字母
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]