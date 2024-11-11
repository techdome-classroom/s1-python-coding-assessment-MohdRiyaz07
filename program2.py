def decode_message( s: str, p: str) -> bool:

# write your code here
        u, v = len(s), len(p)
        dp = [[False] * (v+1) for _ in range(u+1)]
        dp[0][0] = True

        for j in range(1, v+1):
                if p[j - 1]== '*':
                        dp[0][j] = dp[0][j-1]

        for i in range(1, u+1):
                for j in range(1, v+1):
                        if p[j-1] == '*':
                                dp[i][j] = dp[i][j-1] or dp[i-1][j]
                        elif p[j-1] == '?':
                                dp[i][j] = dp[i-1][j-1]
                        else:
                                dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[u][v]